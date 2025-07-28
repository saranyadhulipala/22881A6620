# URL Shortener Microservice

## Features
- Shorten long URLs with optional custom shortcode.
- Tracks number of clicks and IP logs.
- Expiry support (default: 30 mins).
- Middleware logs all requests and responses.

## API Endpoints
### POST /shorturls
Request:
```json
{
  "url": "https://example.com",
  "shortcode": "abc123",
  "validity": 60
}
