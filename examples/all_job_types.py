"""
Example demonstrating all job types available in Edison Scientific.

This example shows how to use:
1. LITERATURE - Literature search
2. ANALYSIS - Data analysis
3. PRECEDENT - Precedent search
4. MOLECULES - Chemistry tasks
"""

import os
from dotenv import load_dotenv
from edison_client import JobNames
from edison_platform import EdisonPlatformClient, JobTypes

# Load environment variables
load_dotenv()


def main():
    """Demonstrate all job types."""
    
    # Initialize the client
    client = EdisonPlatformClient()
    
    print("Edison Platform - All Job Types Demo")
    print("=" * 80)
    
    # 1. LITERATURE Search
    print("\n1. LITERATURE SEARCH")
    print("-" * 80)
    print(f"Description: {JobTypes.get_description(JobTypes.LITERATURE)}")
    
    lit_result = client.literature_search(
        "What are the latest treatments for diabetes?"
    )
    print(f"Result: {lit_result}")
    
    # 2. PRECEDENT Search
    print("\n2. PRECEDENT SEARCH")
    print("-" * 80)
    print(f"Description: {JobTypes.get_description(JobTypes.PRECEDENT)}")
    
    prec_result = client.precedent_search(
        "Has anyone successfully used gene therapy for hemophilia?"
    )
    print(f"Result: {prec_result}")
    
    # 3. DATA ANALYSIS
    print("\n3. DATA ANALYSIS")
    print("-" * 80)
    print(f"Description: {JobTypes.get_description(JobTypes.ANALYSIS)}")
    
    analysis_result = client.analyze_data(
        dataset="example_biological_dataset",
        analysis_type="differential_expression"
    )
    print(f"Result: {analysis_result}")
    
    # 4. CHEMISTRY/MOLECULES
    print("\n4. CHEMISTRY TASKS")
    print("-" * 80)
    print(f"Description: {JobTypes.get_description(JobTypes.MOLECULES)}")
    
    chem_result = client.chemistry_task(
        "Design a small molecule inhibitor for protein kinase X"
    )
    print(f"Result: {chem_result}")
    
    print("\n" + "=" * 80)
    print("Demo completed!")


if __name__ == "__main__":
    main()
