# Edison Platform API - Quick Reference

This is a quick reference guide for using the Edison Platform API integration.

## Installation

```bash
pip install -r requirements.txt
```

## Setup

1. Get your API key from [Edison Scientific](https://www.edisonscientific.com/)
2. Set environment variable:
   ```bash
   export EDISON_API_KEY=your_api_key_here
   ```
   Or create a `.env` file (copy from `.env.example`)

## Basic Usage

```python
from edison_platform import EdisonPlatformClient

# Initialize client
client = EdisonPlatformClient()

# Run a literature search
result = client.literature_search("What are the latest diabetes treatments?")
```

## All Job Types

### 1. Literature Search
Search scientific literature and get cited answers.

```python
result = client.literature_search(
    "Which neglected diseases had a treatment developed by AI?"
)
```

### 2. Precedent Search
Query prior scientific work and discoveries.

```python
result = client.precedent_search(
    "Has anyone used CRISPR to cure sickle cell anemia?"
)
```

### 3. Data Analysis
Analyze biological datasets.

```python
result = client.analyze_data(
    dataset="my_dataset_id",
    analysis_type="differential_expression"
)
```

### 4. Chemistry Tasks
Perform molecular and chemistry tasks.

```python
result = client.chemistry_task(
    "Design a small molecule inhibitor for protein kinase X"
)
```

## Async Usage

```python
import asyncio
from edison_platform import EdisonPlatformClient
from edison_client import JobNames

async def main():
    client = EdisonPlatformClient()
    
    # Run task asynchronously
    result = await client.arun_task({
        "name": JobNames.LITERATURE,
        "query": "What are mechanisms of drug resistance in cancer?"
    })
    print(result)

asyncio.run(main())
```

## Task Management

### Create and Retrieve Tasks

```python
# Create a task
task_id = client.create_task({
    "name": JobNames.PRECEDENT,
    "query": "Recent breakthroughs in Alzheimer's treatment"
})

# Retrieve task result later
result = client.get_task(task_id)
```

### Async Task Management

```python
# Create task asynchronously
task_id = await client.acreate_task(task_data)

# Retrieve asynchronously
result = await client.aget_task(task_id)
```

## Generic Task Execution

For full control, use the generic methods:

```python
from edison_client import JobNames

# Synchronous
result = client.run_task({
    "name": JobNames.LITERATURE,
    "query": "Your scientific question here",
    # Add any other job-specific parameters
})

# Asynchronous
result = await client.arun_task(task_data)
```

## Error Handling

```python
try:
    result = client.literature_search("Your query")
except ValueError as e:
    print(f"Configuration error: {e}")
except Exception as e:
    print(f"Task execution error: {e}")
```

## Available Methods

| Method | Sync/Async | Description |
|--------|------------|-------------|
| `run_task(task_data)` | Sync | Run task until completion |
| `arun_task(task_data)` | Async | Run task asynchronously |
| `create_task(task_data)` | Sync | Create task, get ID |
| `acreate_task(task_data)` | Async | Create task async |
| `get_task(task_id)` | Sync | Get task by ID |
| `aget_task(task_id)` | Async | Get task async |
| `literature_search(query)` | Sync | Convenience: lit search |
| `precedent_search(query)` | Sync | Convenience: precedent |
| `analyze_data(dataset, **kw)` | Sync | Convenience: analysis |
| `chemistry_task(query, **kw)` | Sync | Convenience: chemistry |

## Examples

Run the example scripts:

```bash
# Basic literature search
python examples/basic_literature_search.py

# Advanced async usage
python examples/advanced_async_tasks.py

# All job types demo
python examples/all_job_types.py
```

## Resources

- [Edison Scientific Website](https://www.edisonscientific.com/)
- [Edison Client Docs](https://github.com/Future-House/edison-client-docs)
- [Full README](./README.md)

## Support

For issues:
- **This library**: Open an issue on this repository
- **Edison API**: See [official docs](https://github.com/Future-House/edison-client-docs)
