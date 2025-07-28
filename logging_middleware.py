from flask import request
import datetime

def logging_middleware(app):
    @app.before_request
    def log_request():
        timestamp = datetime.datetime.utcnow().isoformat()
        print(f"[{timestamp}] {request.method} {request.path} - IP: {request.remote_addr}")
