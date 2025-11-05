# Edison Platform API Integration

A Python-based API client integration for the [Edison Scientific](https://www.edisonscientific.com/) platform. This library provides a clean, easy-to-use interface for interacting with Edison's scientific research capabilities including literature search, data analysis, precedent search, and chemistry tasks.

## Features

- **Easy-to-use API client** wrapper around the official `edison-client` library
- **Support for all job types**: LITERATURE, ANALYSIS, PRECEDENT, and MOLECULES
- **Synchronous and asynchronous** task execution
- **Convenience methods** for common tasks
- **Comprehensive examples** demonstrating various use cases
- **Built-in error handling and logging**

## Installation

1. Clone this repository:
```bash
git clone https://github.com/HarleyCoops/EdisonPlatform.git
cd EdisonPlatform
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up your API key:
   - Copy `.env.example` to `.env`
   - Add your Edison API key to the `.env` file:
     ```
     EDISON_API_KEY=your_actual_api_key_here
     ```
   - Get your API key from your [Edison profile page](https://www.edisonscientific.com/)

## Quick Start

### Basic Usage

```python
from edison_platform import EdisonPlatformClient
from edison_client import JobNames

# Initialize the client (reads API key from environment)
client = EdisonPlatformClient()

# Run a literature search
result = client.literature_search(
    "Which neglected diseases had a treatment developed by artificial intelligence?"
)
print(result)
```

### Using Convenience Methods

```python
# Literature search
lit_result = client.literature_search("What are the latest diabetes treatments?")

# Precedent search
prec_result = client.precedent_search("Has anyone used CRISPR to cure sickle cell anemia?")

# Data analysis
analysis_result = client.analyze_data("dataset_id", analysis_type="differential")

# Chemistry tasks
chem_result = client.chemistry_task("Design a drug for target protein X")
```

### Asynchronous Usage

```python
import asyncio
from edison_platform import EdisonPlatformClient
from edison_client import JobNames

async def main():
    client = EdisonPlatformClient()
    
    # Run task asynchronously
    task_data = {
        "name": JobNames.LITERATURE,
        "query": "What are the mechanisms of drug resistance in cancer?"
    }
    result = await client.arun_task(task_data)
    print(result)

asyncio.run(main())
```

### Create and Retrieve Tasks

```python
# Create a task and get its ID
task_id = client.create_task({
    "name": JobNames.PRECEDENT,
    "query": "Recent breakthroughs in Alzheimer's disease treatment"
})

# Retrieve the task result later
result = client.get_task(task_id)
```

## Job Types

Edison Scientific supports four main job types:

| Job Type | Description | Example Use Case |
|----------|-------------|------------------|
| **LITERATURE** | Search and generate answers based on scientific literature | "What are the latest advances in mRNA vaccines?" |
| **ANALYSIS** | Analyze biological datasets | Differential gene expression analysis |
| **PRECEDENT** | Query prior scientific work | "Has anyone used CRISPR for sickle cell anemia?" |
| **MOLECULES** | Chemistry tasks using cheminformatics tools | Drug design, molecular property prediction |

## API Reference

### EdisonPlatformClient

The main client class for interacting with the Edison platform.

#### Methods

- **`__init__(api_key=None)`**: Initialize the client. API key can be passed directly or read from `EDISON_API_KEY` environment variable.

- **`run_task(task_data)`**: Run a task synchronously until completion.
  - **Parameters**: `task_data` (dict) - Task request with `name` and job-specific fields
  - **Returns**: Task response with results

- **`arun_task(task_data)`**: Run a task asynchronously until completion.
  - **Parameters**: `task_data` (dict) - Task request
  - **Returns**: Task response (async)

- **`create_task(task_data)`**: Create and submit a task, returning its ID.
  - **Parameters**: `task_data` (dict) - Task request
  - **Returns**: Task ID (str)

- **`acreate_task(task_data)`**: Create a task asynchronously.
  - **Parameters**: `task_data` (dict) - Task request
  - **Returns**: Task ID (str, async)

- **`get_task(task_id)`**: Retrieve task status and results by ID.
  - **Parameters**: `task_id` (str) - The task ID
  - **Returns**: Task status and results

- **`aget_task(task_id)`**: Retrieve task asynchronously.
  - **Parameters**: `task_id` (str) - The task ID
  - **Returns**: Task status and results (async)

#### Convenience Methods

- **`literature_search(query)`**: Run a literature search task
- **`precedent_search(query)`**: Run a precedent search task
- **`analyze_data(dataset, **kwargs)`**: Run a data analysis task
- **`chemistry_task(query, **kwargs)`**: Run a chemistry task

## Examples

The `examples/` directory contains several demonstration scripts:

1. **`basic_literature_search.py`**: Basic literature search example
   ```bash
   python examples/basic_literature_search.py
   ```

2. **`advanced_async_tasks.py`**: Asynchronous task creation and retrieval
   ```bash
   python examples/advanced_async_tasks.py
   ```

3. **`all_job_types.py`**: Demonstrates all four job types
   ```bash
   python examples/all_job_types.py
   ```

## Project Structure

```
EdisonPlatform/
├── edison_platform/          # Main package
│   ├── __init__.py          # Package initialization
│   ├── client.py            # Main client implementation
│   └── job_types.py         # Job type definitions
├── examples/                 # Example scripts
│   ├── basic_literature_search.py
│   ├── advanced_async_tasks.py
│   └── all_job_types.py
├── requirements.txt          # Python dependencies
├── .env.example             # Example environment configuration
├── .gitignore               # Git ignore rules
└── README.md                # This file
```

## Requirements

- Python 3.7+
- edison-client >= 0.1.0
- python-dotenv >= 1.0.0

## Authentication

To use the Edison Platform API, you need an API key from [Edison Scientific](https://www.edisonscientific.com/). You can provide the API key in two ways:

1. **Environment variable** (recommended):
   ```bash
   export EDISON_API_KEY=your_api_key_here
   ```
   Or use a `.env` file with `python-dotenv`.

2. **Direct initialization**:
   ```python
   client = EdisonPlatformClient(api_key="your_api_key_here")
   ```

## Error Handling

The client includes built-in error handling and logging:

```python
import logging

# Enable logging to see detailed information
logging.basicConfig(level=logging.INFO)

client = EdisonPlatformClient()

try:
    result = client.literature_search("Your query here")
except ValueError as e:
    print(f"Configuration error: {e}")
except Exception as e:
    print(f"Error running task: {e}")
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is provided as-is for integration with the Edison Scientific platform.

## Resources

- [Edison Scientific Website](https://www.edisonscientific.com/)
- [Edison Client Documentation](https://github.com/Future-House/edison-client-docs)
- [Edison API on Postman](https://www.postman.com/Editox)

## Support

For issues related to:
- **This integration library**: Open an issue on this repository
- **Edison platform API**: Refer to the [official Edison documentation](https://github.com/Future-House/edison-client-docs)
- **API access**: Contact Edison Scientific support