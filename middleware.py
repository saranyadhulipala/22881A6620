from flask import request, g
import time

def logging_middleware(app):
    @app.before_request
    def before():
        g.start = time.time()
        print(f"Incoming: {request.method} {request.url}")
        if request.get_json(silent=True):
            print(f"Body: {request.get_json()}")

    @app.after_request
    def after(response):
        duration = time.time() - g.start
        print(f"Response: {response.status} in {duration:.2f}s")
        return response
