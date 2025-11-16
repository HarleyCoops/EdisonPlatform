# Edison Platform

**AI-Accelerated Scientific Discovery**

The Edison Platform provides programmatic access to [Kosmos](https://edisonscientific.com/articles/announcing-kosmos), a next-generation AI Scientist that performs autonomous scientific discovery. Kosmos can accomplish in a single day what would take a PhD or postdoctoral scientist approximately 6 months, reading 1,500 papers and executing 42,000 lines of analysis code in a single run.

## What is Kosmos?

Kosmos is an AI Scientist designed for autonomous discovery. Unlike previous AI systems limited by finite context windows, Kosmos uses structured world models to efficiently incorporate information from hundreds of agent trajectories and maintain coherence over tens of millions of tokens toward specific research objectives.

### Revolutionary Capabilities

- **Scale**: A single Kosmos run reads 1,500 scientific papers and executes 42,000 lines of analysis code
- **Speed**: Beta users estimate Kosmos accomplishes in one day what would take them 6 months
- **Accuracy**: 79.4% of Kosmos conclusions are accurate, validated through replication studies
- **Transparency**: Every conclusion can be traced to specific lines of code or passages in scientific literature
- **Range**: Successfully applied across neuroscience, materials science, statistical genetics, and more

### Real Discoveries

Kosmos has already made seven validated discoveries, including:

- **Reproduced unpublished findings** in metabolomics, identifying nucleotide metabolism as the dominant altered pathway in hypothermic mice brains
- **Novel molecular mechanisms** linking genetic variants to Type 2 diabetes risk reduction
- **Clinically relevant insights** into neuronal vulnerability in aging, identifying reduced flippase expression in entorhinal cortex neurons that may trigger microglia-mediated neurodegeneration in Alzheimer's disease

Read more about Kosmos and its discoveries in the [announcement article](https://edisonscientific.com/articles/announcing-kosmos).

## What Can You Do?

The Edison Platform enables you to:

- **Literature Search**: Query vast scientific literature with citations and traceability
- **Data Analysis**: Perform sophisticated analyses on biological datasets
- **Precedent Search**: Discover prior scientific work and methodologies
- **Chemistry Tasks**: Design molecules, predict properties, and perform cheminformatics analyses
- **Autonomous Discovery**: Run Kosmos on your research objectives to accelerate discovery

## Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Edison API key ([get one here](https://www.edisonscientific.com/))

### Installation

1. Clone the repository:
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

### Basic Usage

```python
from edison_platform import EdisonPlatformClient

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

## Transparency and Traceability

Every conclusion generated by Kosmos can be traced back to its source:

- **Code Provenance**: See exactly which lines of analysis code produced each result
- **Literature Citations**: Trace insights to specific passages in scientific papers
- **Full Audit Trail**: Complete transparency for scientific reproducibility

This ensures that Kosmos reports are fully auditable and meet the standards required for scientific publication.

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

4. **`edison_demo_showcase.py`**: Kosmos-inspired narrative demo (see [`docs/demo-showcase.md`](./docs/demo-showcase.md))
   ```bash
   python examples/edison_demo_showcase.py --dry-run
   ```

## Documentation

Complete documentation is available in the `/docs` directory:

- **[Quick Reference Guide](./docs/quick-reference.md)** - Essential commands and quick tips
- **[Getting Started Guide](./docs/getting-started.md)** - Quick start for new users
- **[API Documentation](./docs/api-documentation.md)** - Complete API reference
- **[API Testing Guide](./docs/api-testing.md)** - How to run API tests
- **[Configuration Guide](./docs/configuration.md)** - Environment setup and configuration
- **[Demo Showcase Guide](./docs/demo-showcase.md)** - How to present the Kosmos walkthrough

## Configuration

The platform uses environment variables for configuration. Key variables:

- `EDISON_API_KEY` - Your API authentication key (required)
- `API_BASE_URL` - Base URL for API requests (optional, defaults to production)
- `API_TIMEOUT` - Request timeout in seconds (optional, default: 30)
- `API_VERIFY_SSL` - Verify SSL certificates (optional, default: true)

See the [Configuration Guide](./docs/configuration.md) for complete details.

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

## Testing

The platform includes a comprehensive API test suite that validates:

1. **Health Check** - Verifies API connectivity
2. **Authentication** - Validates API key configuration
3. **Resources API** - Tests resource listing functionality

Run tests with:
```bash
python tests/api_test.py
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
├── docs/                     # Documentation
│   ├── quick-reference.md
│   ├── getting-started.md
│   ├── api-documentation.md
│   ├── api-testing.md
│   └── configuration.md
├── tests/                    # Test suite
│   └── api_test.py
├── requirements.txt          # Python dependencies
├── .env.example             # Example environment configuration
├── .gitignore               # Git ignore rules
└── README.md                # This file
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Resources

- [Edison Scientific Website](https://www.edisonscientific.com/)
- [Kosmos Announcement](https://edisonscientific.com/articles/announcing-kosmos) - Learn about Kosmos and its discoveries
- [Edison Client Documentation](https://github.com/Future-House/edison-client-docs)
- [Edison API on Postman](https://www.postman.com/Editox)

## Support

For issues related to:
- **This integration library**: Open an issue on this repository
- **Edison platform API**: Refer to the [official Edison documentation](https://github.com/Future-House/edison-client-docs)
- **API access**: Contact Edison Scientific support at support@edisonscientific.com

## License

This project is provided as-is for integration with the Edison Scientific platform.
