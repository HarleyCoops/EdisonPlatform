# Edison Platform

Welcome to the Edison Platform - a comprehensive platform solution with robust API capabilities.

## 📚 Documentation

Complete documentation is available in the `/docs` directory:

- **[Getting Started Guide](./docs/getting-started.md)** - Quick start for new users
- **[API Documentation](./docs/api-documentation.md)** - Complete API reference
- **[API Testing Guide](./docs/api-testing.md)** - How to run API tests
- **[Configuration Guide](./docs/configuration.md)** - Environment setup and configuration

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

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

3. Configure your environment:
```bash
cp .env.example .env
# Edit .env and add your API_KEY and API_BASE_URL
```

### Running API Tests

To test your API configuration:

```bash
python tests/api_test.py
```

Expected output:
```
🔍 Edison Platform API Test Suite
=====================================

Testing configuration...
✅ API_KEY is set
✅ API_BASE_URL is set

🧪 Running API tests...

Test 1: Health Check
  ✅ PASSED

Test 2: Authentication Test
  ✅ PASSED

Test 3: List Resources
  ✅ PASSED

=====================================
Test Results: 3/3 passed
✅ All tests passed successfully!
```

## 🔑 Configuration

The platform uses environment variables for configuration. Key variables:

- `API_KEY` - Your API authentication key (required)
- `API_BASE_URL` - Base URL for API requests (required)
- `API_TIMEOUT` - Request timeout in seconds (optional, default: 30)
- `API_VERIFY_SSL` - Verify SSL certificates (optional, default: true)

See the [Configuration Guide](./docs/configuration.md) for complete details.

## 📖 Documentation Overview

### [Getting Started](./docs/getting-started.md)
Step-by-step guide to set up and run the platform, including:
- Installation instructions
- Environment configuration
- Basic usage examples
- Troubleshooting common issues

### [API Documentation](./docs/api-documentation.md)
Complete API reference including:
- Authentication methods
- Available endpoints
- Request/response examples
- Error handling
- Rate limiting information
- Best practices

### [API Testing Guide](./docs/api-testing.md)
Comprehensive testing documentation covering:
- Running the test suite
- Test case descriptions
- Custom test creation
- CI/CD integration
- Performance testing
- Troubleshooting test failures

### [Configuration Guide](./docs/configuration.md)
Detailed configuration information including:
- Environment variables reference
- Security best practices
- Environment-specific configurations
- Configuration validation
- Secret management

## 🧪 Testing

The platform includes a comprehensive API test suite that validates:

1. **Health Check** - Verifies API connectivity
2. **Authentication** - Validates API key configuration
3. **Resources API** - Tests resource listing functionality

Run tests with:
```bash
python tests/api_test.py
```

## 🔒 Security

- Never commit `.env` files to version control
- Rotate API keys regularly
- Use environment-specific configurations
- Enable SSL verification in production
- Follow the security guidelines in the [Configuration Guide](./docs/configuration.md)

## 📝 Project Structure

```
EdisonPlatform/
├── docs/                      # Documentation
│   ├── README.md             # Documentation index
│   ├── getting-started.md    # Getting started guide
│   ├── api-documentation.md  # API reference
│   ├── api-testing.md        # Testing guide
│   └── configuration.md      # Configuration reference
├── tests/                     # Test suite
│   └── api_test.py           # API test script
├── .env.example              # Environment template
├── .gitignore                # Git ignore rules
├── requirements.txt          # Python dependencies
└── README.md                 # This file
```

## 🤝 Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add/update tests as needed
5. Update documentation
6. Submit a pull request

## 📄 License

See LICENSE file for details.

## 🆘 Support

- Check the [documentation](./docs/) for detailed information
- Review [troubleshooting guides](./docs/getting-started.md#troubleshooting) for common issues
- Open an issue for bugs or feature requests

---

For more information, see the [documentation](./docs/README.md).