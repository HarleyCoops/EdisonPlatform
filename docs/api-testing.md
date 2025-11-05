# API Testing Guide

## Overview

This guide covers how to test the Edison Platform API using the included test suite. The test suite verifies API connectivity, authentication, and core functionality.

## Prerequisites

- Python 3.8 or higher
- API key configured in `.env` file
- Internet connection

## Setup

### 1. Install Test Dependencies

```bash
pip install requests python-dotenv
```

### 2. Configure Environment

Ensure your `.env` file contains the required variables:

```env
API_KEY=your_api_key_here
API_BASE_URL=https://api.example.com/v1
```

## Running Tests

### Run All Tests

Execute the complete test suite:

```bash
python tests/api_test.py
```

### Expected Output

When tests run successfully, you should see:

```
🔍 Edison Platform API Test Suite
=====================================

Testing configuration...
✅ API_KEY is set
✅ API_BASE_URL is set

Running API tests...

Test 1: Health Check
  Endpoint: GET /health
  Status: 200 OK
  ✅ PASSED

Test 2: Authentication Test
  Endpoint: GET /user
  Status: 200 OK
  ✅ PASSED

Test 3: List Resources
  Endpoint: GET /resources
  Status: 200 OK
  ✅ PASSED

=====================================
Test Results: 3/3 passed
✅ All tests passed successfully!
```

## Test Cases

### 1. Health Check Test

**Purpose**: Verify API is reachable and responding

**Endpoint**: `GET /health`

**Expected Result**: 
- Status code: 200
- Response contains `status` field

### 2. Authentication Test

**Purpose**: Verify API key is valid and authentication works

**Endpoint**: `GET /user`

**Expected Result**:
- Status code: 200
- Response contains user information
- Authentication header accepted

### 3. List Resources Test

**Purpose**: Verify ability to retrieve resources

**Endpoint**: `GET /resources`

**Expected Result**:
- Status code: 200
- Response contains data array
- Pagination information included

## Custom Test Configuration

You can customize test behavior by modifying the test script or using environment variables:

### Environment Variables

```env
# Required
API_KEY=your_api_key_here
API_BASE_URL=https://api.example.com/v1

# Optional
API_TIMEOUT=30
API_VERIFY_SSL=true
API_MAX_RETRIES=3
```

### Test Verbosity

For more detailed output, set the verbose flag:

```bash
VERBOSE=true python tests/api_test.py
```

## Troubleshooting

### Connection Errors

**Error**: `Connection refused` or `Timeout`

**Solutions**:
- Verify `API_BASE_URL` is correct
- Check your internet connection
- Verify the API service is running
- Check firewall settings

### Authentication Errors

**Error**: `401 Unauthorized`

**Solutions**:
- Verify `API_KEY` is correct in `.env` file
- Check that the API key hasn't expired
- Ensure the API key has necessary permissions
- Verify the `.env` file is in the project root directory

### SSL Certificate Errors

**Error**: `SSL: CERTIFICATE_VERIFY_FAILED`

**Solutions**:
- Update your CA certificates
- For development only, you can disable SSL verification (not recommended for production):
  ```env
  API_VERIFY_SSL=false
  ```

### Rate Limiting

**Error**: `429 Too Many Requests`

**Solutions**:
- Wait before retrying
- Implement exponential backoff
- Check rate limit headers in responses
- Consider upgrading your API tier

## Writing Custom Tests

### Example: Testing a New Endpoint

```python
import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

API_KEY = os.getenv('API_KEY')
API_BASE_URL = os.getenv('API_BASE_URL')

def test_custom_endpoint():
    """Test a custom endpoint"""
    headers = {
        'Authorization': f'Bearer {API_KEY}'
    }
    
    response = requests.get(
        f'{API_BASE_URL}/custom-endpoint',
        headers=headers
    )
    
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    data = response.json()
    assert 'result' in data, "Response missing 'result' field"
    
    print("✅ Custom endpoint test passed")

if __name__ == '__main__':
    test_custom_endpoint()
```

### Best Practices

1. **Use assertions**: Verify both status codes and response content
2. **Handle errors**: Include try-except blocks for robust tests
3. **Clean up**: Remove test data after tests complete
4. **Isolate tests**: Each test should be independent
5. **Use descriptive names**: Make test purposes clear
6. **Document expected behavior**: Add comments explaining what each test validates

## Continuous Integration

### Running Tests in CI/CD

Example GitHub Actions workflow:

```yaml
name: API Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v2
    
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.8'
    
    - name: Install dependencies
      run: |
        pip install requests python-dotenv
    
    - name: Run API tests
      env:
        API_KEY: ${{ secrets.API_KEY }}
        API_BASE_URL: ${{ secrets.API_BASE_URL }}
      run: python tests/api_test.py
```

## Performance Testing

For load testing, consider using tools like:
- **Apache JMeter**: GUI-based load testing
- **Locust**: Python-based load testing
- **k6**: Modern load testing tool

Example Locust test:

```python
from locust import HttpUser, task, between

class APIUser(HttpUser):
    wait_time = between(1, 3)
    
    def on_start(self):
        self.headers = {
            'Authorization': f'Bearer {os.getenv("API_KEY")}'
        }
    
    @task
    def get_resources(self):
        self.client.get("/resources", headers=self.headers)
```

## Additional Resources

- [API Documentation](./api-documentation.md) - Complete API reference
- [Configuration Guide](./configuration.md) - Environment setup details
- [Getting Started](./getting-started.md) - Initial setup guide

## Support

For test-related issues:
1. Check test output for specific error messages
2. Review the troubleshooting section above
3. Verify your configuration in `.env`
4. Open an issue with test output and configuration details (excluding sensitive data)
