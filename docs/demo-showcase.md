# Kosmos Demo Showcase

This guide packages the Edison Platform repository into a quick, story-driven demo
that mirrors the [Kosmos announcement](https://edisonscientific.com/articles/announcing-kosmos).
It is designed for sharing with collaborators or for educational walk-throughs.

## Why this narrative resonates

From the announcement:

- **Structured world models** keep hundreds of agent trajectories coherent across tens of millions of tokens, letting Kosmos trace every conclusion back to specific code or literature snippets.
- **Scale**: a single Kosmos run routinely reads ~1,500 papers and executes ~42,000 lines of analysis code.
- **Impact**: beta testers report Kosmos completes six months of work in a day with 79.4% accurate conclusions, enabling discoveries in metabolomics, materials science, statistical genetics, and neurodegeneration.

The new `examples/edison_demo_showcase.py` fast-tracks those talking points into four “scenes” that map to the discoveries introduced in the blog post.

## Running the walkthrough

1. Install dependencies (including `python-dotenv`) if you haven’t already:
   ```bash
   pip install -r requirements.txt
   ```

2. Provide your Edison API key, either in the shell or in `.env`:
   ```bash
   export EDISON_API_KEY=your_key   # or set it in .env
   ```

3. Run the showcase. Use `--dry-run` when you only want the narration; omit it to hit the live API:
   ```bash
   python examples/edison_demo_showcase.py --dry-run
   python examples/edison_demo_showcase.py          # live run
   ```

Useful CLI switches:

- `--list-scenes` – prints all available scene IDs.
- `--scenes hypothermia-metabolomics perovskite-humidity` – limit the demo to particular beats.
- `--dry-run` – narrate without needing credentials (handy for large audiences).

## Scene guide

| Scene ID | Job type | Kosmos connection |
| --- | --- | --- |
| `hypothermia-metabolomics` | `LITERATURE` | Reproduces the metabolomics discovery that nucleotide metabolism dominates in hypothermic mice brains—even before the original paper reached BioRxiv. |
| `perovskite-humidity` | `PRECEDENT` | Recaps the perovskite “fatal filter” insight showing absolute humidity (~60 g/m³) governs thermal annealing success. |
| `sod2-mendelian` | `ANALYSIS` | Walks through the GWAS+pQTL Mendelian randomization that linked elevated circulating SOD2 to reduced myocardial fibrosis in humans. |
| `flippase-vulnerability` | `MOLECULES` | Extends Kosmos’ entorhinal-cortex finding by asking the chemistry stack to design flippase-sustaining interventions that could mask phosphatidylserine “eat me” signals. |

Each scene prints:

- A short insight pulled directly from the public announcement.
- The JSON payload sent to Edison (so viewers see how little boilerplate is required).
- Either a placeholder message (`--dry-run`) or the actual response from the `EdisonPlatformClient`.

## Presenting tips

- **Lead with the highlights**: the script opens with the same facts the article emphasized (world models, 1,500 papers, 42,000 LOC, six-month compression). Pause there before running the code so your audience has the right frame.
- **Show provenance**: when you run live, scroll up to the JSON payload and point out how each parameter mirrors the question you would ask a colleague.
- **Invite remixing**: encourage the audience to duplicate `SCENES` entries in `examples/edison_demo_showcase.py` with their own objectives—no new plumbing required.
- **Connect to docs**: follow up with references to `docs/quick-reference.md` and `docs/api-documentation.md` so viewers know where to dive deeper after the show-and-tell.
