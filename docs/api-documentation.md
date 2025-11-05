# API Documentation

## Overview

The Edison Platform API provides programmatic access to platform features and services. This document describes the available endpoints, authentication methods, and usage examples.

## Base URL

```
https://api.example.com/v1
```

The base URL can be configured via the `API_BASE_URL` environment variable.

## Authentication

All API requests require authentication using an API key. Include your API key in the request headers:

```
Authorization: Bearer YOUR_API_KEY
```

### Getting an API Key

1. Register for an account at the platform portal
2. Navigate to API settings
3. Generate a new API key
4. Store the key securely in your `.env` file

## Endpoints

### Health Check

Check the API status and connectivity.

**Endpoint**: `GET /health`

**Headers**: None required

**Response**:
```json
{
  "status": "ok",
  "timestamp": "2025-11-05T15:16:33.582Z",
  "version": "1.0.0"
}
```

**Example**:
```bash
curl https://api.example.com/v1/health
```

### Get User Information

Retrieve authenticated user information.

**Endpoint**: `GET /user`

**Headers**:
- `Authorization: Bearer YOUR_API_KEY`

**Response**:
```json
{
  "id": "user_123",
  "email": "user@example.com",
  "name": "John Doe",
  "created_at": "2025-01-01T00:00:00Z"
}
```

**Example**:
```bash
curl -H "Authorization: Bearer YOUR_API_KEY" \
     https://api.example.com/v1/user
```

### Create Resource

Create a new resource in the platform.

**Endpoint**: `POST /resources`

**Headers**:
- `Authorization: Bearer YOUR_API_KEY`
- `Content-Type: application/json`

**Request Body**:
```json
{
  "name": "My Resource",
  "description": "Resource description",
  "type": "standard"
}
```

**Response**:
```json
{
  "id": "resource_456",
  "name": "My Resource",
  "description": "Resource description",
  "type": "standard",
  "created_at": "2025-11-05T15:16:33.582Z",
  "status": "active"
}
```

**Example**:
```bash
curl -X POST \
     -H "Authorization: Bearer YOUR_API_KEY" \
     -H "Content-Type: application/json" \
     -d '{"name":"My Resource","description":"Test resource","type":"standard"}' \
     https://api.example.com/v1/resources
```

### List Resources

Retrieve a list of resources.

**Endpoint**: `GET /resources`

**Headers**:
- `Authorization: Bearer YOUR_API_KEY`

**Query Parameters**:
- `page` (optional): Page number for pagination (default: 1)
- `limit` (optional): Number of results per page (default: 10, max: 100)
- `type` (optional): Filter by resource type

**Response**:
```json
{
  "data": [
    {
      "id": "resource_456",
      "name": "My Resource",
      "type": "standard",
      "created_at": "2025-11-05T15:16:33.582Z"
    }
  ],
  "pagination": {
    "page": 1,
    "limit": 10,
    "total": 1,
    "pages": 1
  }
}
```

**Example**:
```bash
curl -H "Authorization: Bearer YOUR_API_KEY" \
     "https://api.example.com/v1/resources?page=1&limit=10"
```

### Get Resource Details

Get detailed information about a specific resource.

**Endpoint**: `GET /resources/{resource_id}`

**Headers**:
- `Authorization: Bearer YOUR_API_KEY`

**Response**:
```json
{
  "id": "resource_456",
  "name": "My Resource",
  "description": "Resource description",
  "type": "standard",
  "created_at": "2025-11-05T15:16:33.582Z",
  "updated_at": "2025-11-05T15:16:33.582Z",
  "status": "active",
  "metadata": {}
}
```

**Example**:
```bash
curl -H "Authorization: Bearer YOUR_API_KEY" \
     https://api.example.com/v1/resources/resource_456
```

### Update Resource

Update an existing resource.

**Endpoint**: `PATCH /resources/{resource_id}`

**Headers**:
- `Authorization: Bearer YOUR_API_KEY`
- `Content-Type: application/json`

**Request Body**:
```json
{
  "name": "Updated Resource Name",
  "description": "Updated description"
}
```

**Response**:
```json
{
  "id": "resource_456",
  "name": "Updated Resource Name",
  "description": "Updated description",
  "type": "standard",
  "updated_at": "2025-11-05T15:16:33.582Z"
}
```

### Delete Resource

Delete a resource.

**Endpoint**: `DELETE /resources/{resource_id}`

**Headers**:
- `Authorization: Bearer YOUR_API_KEY`

**Response**:
```json
{
  "message": "Resource deleted successfully",
  "id": "resource_456"
}
```

**Example**:
```bash
curl -X DELETE \
     -H "Authorization: Bearer YOUR_API_KEY" \
     https://api.example.com/v1/resources/resource_456
```

## Error Handling

The API uses standard HTTP status codes:

- `200 OK`: Request succeeded
- `201 Created`: Resource created successfully
- `400 Bad Request`: Invalid request parameters
- `401 Unauthorized`: Missing or invalid API key
- `403 Forbidden`: Insufficient permissions
- `404 Not Found`: Resource not found
- `429 Too Many Requests`: Rate limit exceeded
- `500 Internal Server Error`: Server error

### Error Response Format

```json
{
  "error": {
    "code": "invalid_request",
    "message": "The request parameters are invalid",
    "details": "Field 'name' is required"
  }
}
```

## Rate Limiting

API requests are rate limited to:
- 100 requests per minute for authenticated users
- 10 requests per minute for unauthenticated endpoints

Rate limit information is included in response headers:
- `X-RateLimit-Limit`: Maximum requests per window
- `X-RateLimit-Remaining`: Remaining requests in current window
- `X-RateLimit-Reset`: Timestamp when the rate limit resets

## Best Practices

1. **Store API keys securely**: Never commit API keys to version control
2. **Handle errors gracefully**: Implement proper error handling and retries
3. **Respect rate limits**: Implement exponential backoff for retries
4. **Use HTTPS**: Always use HTTPS for API requests
5. **Keep dependencies updated**: Regularly update client libraries
6. **Log requests**: Keep logs for debugging and monitoring

## SDKs and Libraries

### Python

```python
from edison_platform import Client

client = Client(api_key="your_api_key")
resources = client.resources.list()
```

### JavaScript

```javascript
const Edison = require('edison-platform');

const client = new Edison({ apiKey: 'your_api_key' });
const resources = await client.resources.list();
```

## Support

For API support:
- Check the [API Testing Guide](./api-testing.md) for testing tools
- Review the [Configuration Guide](./configuration.md) for setup help
- Open an issue in the repository for bugs or feature requests
