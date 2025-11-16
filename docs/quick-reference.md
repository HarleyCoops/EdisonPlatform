# Quick Reference Guide

## Essential Commands

### Setup
```bash
# Clone repository
git clone https://github.com/HarleyCoops/EdisonPlatform.git
cd EdisonPlatform

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env with your API credentials
```

### Running Tests
```bash
# Run API test suite
python tests/api_test.py

# Run with verbose output
VERBOSE=true python tests/api_test.py
```

## Environment Variables

### Required
| Variable | Description | Example |
|----------|-------------|---------|
| `API_KEY` | Your API authentication key | `sk_live_abc123...` |
| `API_BASE_URL` | Base URL for API requests | `https://api.example.com/v1` |

### Optional
| Variable | Description | Default |
|----------|-------------|---------|
| `API_TIMEOUT` | Request timeout (seconds) | `30` |
| `API_VERIFY_SSL` | Verify SSL certificates | `true` |
| `API_MAX_RETRIES` | Maximum retry attempts | `3` |
| `LOG_LEVEL` | Logging verbosity | `INFO` |
| `ENVIRONMENT` | Environment identifier | `development` |

## API Test Suite

### Test Cases
1. **Health Check** - Verifies API connectivity
2. **Authentication** - Validates API key
3. **List Resources** - Tests resource retrieval

### Expected Output
```
Edison Platform API Test Suite
=====================================

Testing configuration...
API_KEY is set
API_BASE_URL is set

Running API tests...

Test 1: Health Check
  PASSED

Test 2: Authentication Test
  PASSED

Test 3: List Resources
  PASSED

=====================================
Test Results: 3/3 passed
All tests passed successfully!
```

## Troubleshooting

### Configuration Errors
```bash
# Verify .env file exists
ls -la .env

# Check .env contents (be careful not to expose in logs)
cat .env

# Validate configuration
python -c "from dotenv import load_dotenv; import os; load_dotenv(); print('API_KEY:', 'set' if os.getenv('API_KEY') else 'not set')"
```

### Connection Issues
```bash
# Test network connectivity
curl -I https://api.example.com/v1/health

# Check DNS resolution
nslookup api.example.com

# Test with verbose output
curl -v https://api.example.com/v1/health
```

### SSL Certificate Issues
```bash
# Update CA certificates
pip install --upgrade certifi

# Test SSL connection
openssl s_client -connect api.example.com:443 -servername api.example.com
```

## Common Tasks

### Update Dependencies
```bash
pip install --upgrade -r requirements.txt
```

### Check Python Version
```bash
python --version  # Should be 3.8 or higher
```

### View Logs
```bash
# Set verbose logging
export LOG_LEVEL=DEBUG
python tests/api_test.py
```

## Project Structure

```
EdisonPlatform/
├── docs/                      # Documentation
│   ├── README.md             # Documentation index
│   ├── getting-started.md    # Setup guide
│   ├── api-documentation.md  # API reference
│   ├── api-testing.md        # Testing guide
│   ├── configuration.md      # Config reference
│   └── quick-reference.md    # This file
├── tests/                     # Test suite
│   └── api_test.py           # API tests
├── .env.example              # Config template
├── .gitignore                # Git ignore rules
├── requirements.txt          # Python dependencies
└── README.md                 # Main documentation
```

## Documentation Links

- [Full Documentation Index](./README.md)
- [Getting Started Guide](./getting-started.md)
- [API Documentation](./api-documentation.md)
- [API Testing Guide](./api-testing.md)
- [Configuration Guide](./configuration.md)

## Support

1. Check documentation in `/docs` directory
2. Review troubleshooting sections
3. Verify environment configuration
4. Check API status
5. Open an issue with details

## Quick Tips

- Always use `.env` file for credentials (never hardcode)
- Keep dependencies updated
- Test locally before deploying
- Enable SSL verification in production
- Rotate API keys regularly
- Monitor rate limits
- Use appropriate timeouts
- Log errors for debugging

## Status Codes

| Code | Meaning | Action |
|------|---------|--------|
| 200 | Success | Continue |
| 401 | Unauthorized | Check API_KEY |
| 403 | Forbidden | Verify permissions |
| 404 | Not Found | Check endpoint URL |
| 429 | Rate Limited | Wait and retry |
| 500 | Server Error | Check API status |
