# Getting Started with Edison Platform

## Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.8 or higher
- pip (Python package manager)
- Git

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/HarleyCoops/EdisonPlatform.git
cd EdisonPlatform
```

### 2. Set Up Environment

Create a virtual environment (recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Copy the example environment file:

```bash
cp .env.example .env
```

Edit `.env` and add your API key:

```
API_KEY=your_api_key_here
API_BASE_URL=https://api.example.com
```

**Important**: Never commit the `.env` file to version control. It contains sensitive information.

## Running the Platform

### Basic Usage

```bash
python main.py
```

### Running API Tests

To verify your setup is working correctly:

```bash
python tests/api_test.py
```

See the [API Testing Guide](./api-testing.md) for more details.

## Next Steps

- Read the [API Documentation](./api-documentation.md) to understand available endpoints
- Review the [Configuration Guide](./configuration.md) for advanced settings
- Check the [API Testing Guide](./api-testing.md) for testing best practices

## Troubleshooting

### Common Issues

**Issue**: `ModuleNotFoundError`
- **Solution**: Make sure you've installed dependencies with `pip install -r requirements.txt`

**Issue**: API key not working
- **Solution**: Verify your API key is correctly set in the `.env` file

**Issue**: Connection errors
- **Solution**: Check your internet connection and verify the API_BASE_URL is correct

## Getting Help

If you encounter issues not covered here:
1. Check existing issues in the repository
2. Review the full documentation in the `/docs` directory
3. Open a new issue with details about your problem
