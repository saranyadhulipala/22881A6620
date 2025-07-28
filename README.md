# Logging Middleware

This folder contains a reusable Flask middleware component that logs all incoming HTTP requests with method, path, timestamp, and client IP.

## How it works

- Logs request method, path, and IP using `@app.before_request`
- UTC timestamp is added for audit traceability

## Usage

```python
from logging_middleware import logging_middleware
logging_middleware(app)
