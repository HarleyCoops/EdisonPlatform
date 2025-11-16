#!/usr/bin/env python3
"""
Edison Platform showcase inspired by the Kosmos announcement.

This demo script strings together a narrative walkthrough of how researchers
can lean on Kosmos-powered workflows inside the Edison Platform, highlighting
discoveries that were described in the public announcement:
https://edisonscientific.com/articles/announcing-kosmos
"""

from __future__ import annotations

import argparse
import json
import textwrap
from typing import Any, Dict, Iterable, List

from dotenv import load_dotenv

from edison_platform import EdisonPlatformClient
from edison_platform.job_types import JobTypes


HIGHLIGHTS: List[str] = [
    (
        "Structured world models let Kosmos stitch together hundreds of agent "
        "trajectories, keep tens of millions of tokens in scope, and audit every "
        "conclusion back to the code and literature that produced it."
    ),
    (
        "A single Kosmos run routinely reads ~1,500 papers and executes ~42,000 "
        "lines of analysis code. Beta testers report that compresses six months "
        "of effort into a day with 79.4% accurate conclusions."
    ),
    (
        "Seven discoveries already span metabolomics, materials science, "
        "statistical genetics, and neurodegeneration - each fully traceable "
        "through the Edison Platform."
    ),
]


Scene = Dict[str, Any]

SCENES: List[Scene] = [
    {
        "id": "hypothermia-metabolomics",
        "title": "Validate metabolic shifts in hypothermic brains",
        "insight": (
            "Kosmos reproduced a metabolomics claim that nucleotide metabolism is "
            "the dominant altered pathway in hypothermic mice brains, even before "
            "the originating paper hit BioRxiv."
        ),
        "method": "literature_search",
        "kwargs": {
            "query": (
                "Metabolomics evidence that nucleotide metabolism shifts dominate "
                "hypothermic mouse brains; surface the strongest datasets and code "
                "snippets that support or refute the claim."
            )
        },
        "job_type": JobTypes.LITERATURE,
    },
    {
        "id": "perovskite-humidity",
        "title": "Stress-test perovskite fabrication assumptions",
        "insight": (
            "In materials science, Kosmos rediscovered that absolute humidity "
            "during thermal annealing - especially the ~60 g/m^3 fatal filter - "
            "governs perovskite solar cell efficiency."
        ),
        "method": "precedent_search",
        "kwargs": {
            "query": (
                "Evidence that absolute humidity >60 g/m^3 during perovskite "
                "thermal annealing kills device performance; retrieve the fatal "
                "filter threshold analysis."
            )
        },
        "job_type": JobTypes.PRECEDENT,
    },
    {
        "id": "sod2-mendelian",
        "title": "Combine GWAS + pQTL to reason about fibrosis",
        "insight": (
            "Kosmos ran a Mendelian randomization showing that elevated circulating "
            "SOD2 may causally reduce myocardial T1 times and fibrosis, extending "
            "mouse results into humans."
        ),
        "method": "analyze_data",
        "kwargs": {
            "dataset": "public_gwas_mri_bundle",
            "analysis_type": "mendelian_randomization",
            "exposure": "plasma superoxide dismutase 2",
            "outcome": "myocardial T1 time / fibrosis markers",
            "notes": (
                "Use shared GWAS + pQTL panels; prioritize effect estimates with "
                "leave-one-out stability."
            ),
        },
        "job_type": JobTypes.ANALYSIS,
    },
    {
        "id": "flippase-vulnerability",
        "title": "Design a rescue hypothesis for aging neurons",
        "insight": (
            "Kosmos found that aging entorhinal cortex neurons lose flippase "
            "expression, exposing phosphatidylserine 'eat me' signals. Here we "
            "ask for a chemistry angle to stabilize those neurons."
        ),
        "method": "chemistry_task",
        "kwargs": {
            "query": (
                "Suggest tractable small molecules or biologics that could sustain "
                "ATP11C/ATP8A1 flippase activity in aging entorhinal neurons to "
                "mask phosphatidylserine exposure."
            ),
            "constraints": {
                "delivery": "CNS penetrant",
                "safety_focus": "microglial activation minimization",
            },
        },
        "job_type": JobTypes.MOLECULES,
    },
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Narrated Edison Platform showcase inspired by Kosmos."
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print the narrative without executing live API calls.",
    )
    parser.add_argument(
        "--scenes",
        nargs="+",
        metavar="SCENE_ID",
        help="Limit the walkthrough to specific scene IDs.",
    )
    parser.add_argument(
        "--list-scenes",
        action="store_true",
        help="List available scenes and exit.",
    )
    return parser.parse_args()


def format_json(data: Any) -> str:
    """Render responses in a readable JSON block when possible."""
    try:
        return json.dumps(data, indent=2, default=str)
    except TypeError:
        return str(data)


def iter_scenes(selected_ids: Iterable[str] | None) -> Iterable[Scene]:
    if not selected_ids:
        return SCENES
    allowed = {scene_id.lower() for scene_id in selected_ids}
    return [scene for scene in SCENES if scene["id"].lower() in allowed]


def print_header() -> None:
    print("\nEdison Platform x Kosmos Showcase")
    print("=" * 80)
    for bullet in HIGHLIGHTS:
        print(f"- {textwrap.fill(bullet, width=78, subsequent_indent='  ')}")
    print("=" * 80)


def run_scene(scene: Scene, client: EdisonPlatformClient | None, dry_run: bool) -> None:
    print(f"\n[{scene['id']}] {scene['title']}")
    print("-" * 80)
    print(textwrap.fill(scene["insight"], width=80))
    print("\nJob type:", scene["job_type"].name)
    print("Payload:")
    print(format_json(scene["kwargs"]))

    if dry_run or client is None:
        print("\nDry-run mode: skipping live Edison API call.")
        return

    method = getattr(client, scene["method"])
    print("\nRunning on Edison...")
    response = method(**scene["kwargs"])
    print("\nResponse:")
    print(format_json(response))


def list_available_scenes() -> None:
    print("Available scenes:\n")
    for scene in SCENES:
        print(f"- {scene['id']}: {scene['title']}")


def main() -> None:
    args = parse_args()

    if args.list_scenes:
        list_available_scenes()
        return

    selected_scenes = list(iter_scenes(args.scenes))
    if args.scenes and not selected_scenes:
        raise SystemExit("No scenes matched the provided IDs.")

    load_dotenv()

    client: EdisonPlatformClient | None = None
    if not args.dry_run:
        try:
            client = EdisonPlatformClient()
        except ValueError as exc:
            raise SystemExit(
                f"{exc}\nSet EDISON_API_KEY or rerun with --dry-run to preview the demo."
            ) from exc

    print_header()
    for scene in selected_scenes:
        run_scene(scene, client, dry_run=args.dry_run)

    print("\nDemo complete. Invite your audience to try their own scene next!")


if __name__ == "__main__":
    main()
