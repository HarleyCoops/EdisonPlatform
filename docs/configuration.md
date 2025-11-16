# Configuration Guide

## Overview

This guide covers all configuration options for the Edison Platform, including environment variables, API settings, and deployment configurations.

## Environment Variables

### Required Variables

These variables must be set for the platform to function:

#### API_KEY

Your API authentication key.

```env
API_KEY=your_api_key_here
```

- **Type**: String
- **Required**: Yes
- **Description**: Authentication key for API requests
- **Security**: Never commit this to version control
- **How to obtain**: Generate from the platform dashboard

#### API_BASE_URL

The base URL for API requests.

```env
API_BASE_URL=https://api.example.com/v1
```

- **Type**: URL
- **Required**: Yes
- **Default**: None
- **Description**: Base endpoint for all API requests
- **Common values**:
  - Production: `https://api.example.com/v1`
  - Staging: `https://staging-api.example.com/v1`
  - Development: `http://localhost:3000/v1`

### Optional Variables

#### API_TIMEOUT

Request timeout in seconds.

```env
API_TIMEOUT=30
```

- **Type**: Integer
- **Required**: No
- **Default**: 30
- **Description**: Maximum time to wait for API responses
- **Range**: 5-300 seconds

#### API_VERIFY_SSL

Enable or disable SSL certificate verification.

```env
API_VERIFY_SSL=true
```

- **Type**: Boolean (true/false)
- **Required**: No
- **Default**: true
- **Description**: Whether to verify SSL certificates
- **Note**: Only set to false in development environments

#### API_MAX_RETRIES

Maximum number of retry attempts for failed requests.

```env
API_MAX_RETRIES=3
```

- **Type**: Integer
- **Required**: No
- **Default**: 3
- **Description**: Number of times to retry failed requests
- **Range**: 0-10

#### LOG_LEVEL

Logging verbosity level.

```env
LOG_LEVEL=INFO
```

- **Type**: String
- **Required**: No
- **Default**: INFO
- **Options**: DEBUG, INFO, WARNING, ERROR, CRITICAL
- **Description**: Controls the amount of logging output

#### ENVIRONMENT

Deployment environment identifier.

```env
ENVIRONMENT=production
```

- **Type**: String
- **Required**: No
- **Default**: development
- **Options**: development, staging, production
- **Description**: Identifies the current deployment environment

## Configuration Files

### .env File

The `.env` file stores environment-specific configuration:

```env
# API Configuration
API_KEY=your_api_key_here
API_BASE_URL=https://api.example.com/v1
API_TIMEOUT=30
API_VERIFY_SSL=true

# Application Settings
ENVIRONMENT=production
LOG_LEVEL=INFO

# Optional Settings
API_MAX_RETRIES=3
```

**Location**: Project root directory

**Security**: 
- Never commit `.env` to version control
- Use `.env.example` as a template
- Restrict file permissions: `chmod 600 .env`

### .env.example File

Template file that can be safely committed to version control:

```env
# API Configuration
API_KEY=your_api_key_here
API_BASE_URL=https://api.example.com/v1

# Application Settings
ENVIRONMENT=development
LOG_LEVEL=INFO
```

**Usage**:
```bash
cp .env.example .env
# Edit .env with your actual values
```

## Environment-Specific Configurations

### Development Environment

```env
API_KEY=dev_api_key
API_BASE_URL=http://localhost:3000/v1
API_VERIFY_SSL=false
ENVIRONMENT=development
LOG_LEVEL=DEBUG
```

**Characteristics**:
- Local API endpoint
- SSL verification disabled
- Verbose logging
- Shorter timeouts for faster feedback

### Staging Environment

```env
API_KEY=staging_api_key
API_BASE_URL=https://staging-api.example.com/v1
API_VERIFY_SSL=true
ENVIRONMENT=staging
LOG_LEVEL=INFO
```

**Characteristics**:
- Staging API endpoint
- SSL verification enabled
- Standard logging
- Production-like configuration

### Production Environment

```env
API_KEY=prod_api_key
API_BASE_URL=https://api.example.com/v1
API_VERIFY_SSL=true
API_TIMEOUT=30
API_MAX_RETRIES=3
ENVIRONMENT=production
LOG_LEVEL=WARNING
```

**Characteristics**:
- Production API endpoint
- All security features enabled
- Error-level logging only
- Optimized retry logic

## Security Best Practices

### Protecting Sensitive Data

1. **Never commit secrets**: Add `.env` to `.gitignore`
2. **Use environment variables**: Don't hardcode credentials
3. **Rotate keys regularly**: Update API keys periodically
4. **Limit key permissions**: Use least-privilege principle
5. **Encrypt at rest**: Use encrypted storage for production secrets

### .gitignore Configuration

Ensure your `.gitignore` includes:

```gitignore
# Environment files
.env
.env.local
.env.*.local

# Sensitive data
*.key
*.pem
secrets/
```

### Secret Management

For production deployments, consider using:

- **AWS Secrets Manager**: For AWS deployments
- **Azure Key Vault**: For Azure deployments
- **Google Secret Manager**: For GCP deployments
- **HashiCorp Vault**: For on-premise or multi-cloud
- **Environment variables**: In container orchestration (Kubernetes, Docker)

## Loading Configuration

### Python Example

```python
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Access configuration
API_KEY = os.getenv('API_KEY')
API_BASE_URL = os.getenv('API_BASE_URL')

try:
    API_TIMEOUT = int(os.getenv('API_TIMEOUT', 30))
except ValueError:
    print("Warning: API_TIMEOUT must be an integer. Using default: 30")
    API_TIMEOUT = 30

API_VERIFY_SSL = os.getenv('API_VERIFY_SSL', 'true').lower() != 'false'

# Validate required variables
if not API_KEY:
    raise ValueError("API_KEY environment variable is required")
if not API_BASE_URL:
    raise ValueError("API_BASE_URL environment variable is required")
```

### JavaScript Example

```javascript
require('dotenv').config();

// Access configuration
const config = {
  apiKey: process.env.API_KEY,
  apiBaseUrl: process.env.API_BASE_URL,
  apiTimeout: parseInt(process.env.API_TIMEOUT || '30'),
  apiVerifySSL: process.env.API_VERIFY_SSL !== 'false'
};

// Validate required variables
if (!config.apiKey) {
  throw new Error('API_KEY environment variable is required');
}
if (!config.apiBaseUrl) {
  throw new Error('API_BASE_URL environment variable is required');
}

module.exports = config;
```

## Troubleshooting

### Configuration Not Loading

**Problem**: Environment variables not accessible

**Solutions**:
1. Verify `.env` file exists in project root
2. Check file permissions
3. Ensure `load_dotenv()` is called before accessing variables
4. Verify no typos in variable names

### Invalid Configuration Values

**Problem**: Application fails with configuration errors

**Solutions**:
1. Verify all required variables are set
2. Check variable formats (URLs, numbers, booleans)
3. Ensure no extra whitespace in values
4. Validate against `.env.example` template

### SSL Certificate Issues

**Problem**: SSL verification failures

**Solutions**:
1. Update CA certificates: `pip install --upgrade certifi`
2. For development only: Set `API_VERIFY_SSL=false`
3. Check system date/time is correct
4. Verify API endpoint URL is correct (https vs http)

## Validation

### Configuration Validation Script

Create a script to validate configuration:

```python
import os
from dotenv import load_dotenv

def validate_config():
    """Validate all required configuration is present"""
    load_dotenv()
    
    required = ['API_KEY', 'API_BASE_URL']
    missing = [var for var in required if not os.getenv(var)]
    
    if missing:
        print(f"Missing required variables: {', '.join(missing)}")
        return False
    
    print("All required configuration variables are set")
    return True

if __name__ == '__main__':
    validate_config()
```

## Additional Resources

- [Getting Started](./getting-started.md) - Initial setup guide
- [API Testing Guide](./api-testing.md) - Testing configuration
- [API Documentation](./api-documentation.md) - API usage details
