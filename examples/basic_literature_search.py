"""
Basic example of using the Edison Platform Client for literature search.

This example demonstrates how to:
1. Initialize the client with an API key
2. Run a simple literature search task
3. Handle the response
"""

import os
from dotenv import load_dotenv
from edison_client import JobNames
from edison_platform import EdisonPlatformClient

# Load environment variables from .env file
load_dotenv()

def main():
    """Run a basic literature search example."""
    
    # Initialize the client
    # The API key will be read from the EDISON_API_KEY environment variable
    client = EdisonPlatformClient()
    
    # Define a literature search task
    query = "Which neglected diseases had a treatment developed by artificial intelligence?"
    
    print(f"Running literature search: {query}")
    print("-" * 80)
    
    # Method 1: Using the convenience method
    response = client.literature_search(query)
    
    print("Response received:")
    print(response)
    print("-" * 80)
    
    # Method 2: Using the generic run_task method
    task_data = {
        "name": JobNames.LITERATURE,
        "query": "What are the latest advances in mRNA vaccine technology?"
    }
    
    print(f"\nRunning another literature search: {task_data['query']}")
    print("-" * 80)
    
    response2 = client.run_task(task_data)
    
    print("Response received:")
    print(response2)


if __name__ == "__main__":
    main()
