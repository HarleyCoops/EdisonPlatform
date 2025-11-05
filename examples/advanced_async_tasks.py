"""
Advanced example demonstrating asynchronous task creation and retrieval.

This example shows how to:
1. Create tasks asynchronously
2. Retrieve task status and results later
3. Handle multiple tasks concurrently
"""

import asyncio
import os
from dotenv import load_dotenv
from edison_client import JobNames
from edison_platform import EdisonPlatformClient

# Load environment variables
load_dotenv()


async def main():
    """Run advanced async examples."""
    
    # Initialize the client
    client = EdisonPlatformClient()
    
    # Example 1: Create a task and poll for results
    print("Example 1: Create and retrieve task")
    print("-" * 80)
    
    task_data = {
        "name": JobNames.PRECEDENT,
        "query": "Has anyone used CRISPR to cure sickle cell anemia?"
    }
    
    # Create the task
    task_id = await client.acreate_task(task_data)
    print(f"Task created with ID: {task_id}")
    
    # Retrieve the task result
    # In a real scenario, you might poll this or wait before retrieving
    result = await client.aget_task(task_id)
    print(f"Task result: {result}")
    print("-" * 80)
    
    # Example 2: Run multiple tasks concurrently
    print("\nExample 2: Run multiple tasks concurrently")
    print("-" * 80)
    
    tasks = [
        {
            "name": JobNames.LITERATURE,
            "query": "What are the mechanisms of drug resistance in cancer?"
        },
        {
            "name": JobNames.PRECEDENT,
            "query": "What are recent breakthroughs in Alzheimer's disease treatment?"
        }
    ]
    
    # Run all tasks concurrently
    results = await asyncio.gather(
        *[client.arun_task(task) for task in tasks]
    )
    
    for i, result in enumerate(results, 1):
        print(f"\nTask {i} result:")
        print(result)
        print("-" * 40)


if __name__ == "__main__":
    asyncio.run(main())
