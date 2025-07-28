from flask import Flask, request, jsonify, redirect
from middleware import logging_middleware
from storage import store_url, get_url, log_click, get_stats, is_expired
#from utils import generate_shortcode, current_time_plus_minutes
import datetime
from utils import generate_shortcode


app = Flask(__name__)
logging_middleware(app)

@app.route("/shorturls", methods=["POST"])
def create_short_url():
    data = request.get_json()
    url = data.get("url")
    validity = data.get("validity", 30)
    shortcode = data.get("shortcode", generate_shortcode())

    if not url:
        return jsonify({"error": "URL is required"}), 400

    success, result = store_url(shortcode, url, validity)
    if not success:
        return jsonify({"error": result}), 409

    return jsonify({
        "shortLink": f"http://localhost:5000/{shortcode}",
        "expiry": result
    })

@app.route("/shorturls/<shortcode>", methods=["GET"])
def stats(shortcode):
    stats = get_stats(shortcode)
    if not stats:
        return jsonify({"error": "Shortcode not found"}), 404
    return jsonify(stats)

@app.route("/<shortcode>", methods=["GET"])
def redirect_url(shortcode):
    entry = get_url(shortcode)
    if not entry:
        return jsonify({"error": "Shortcode not found"}), 404
    if is_expired(entry['expiry']):
        return jsonify({"error": "Link expired"}), 410

    log_click(shortcode, request)
    return redirect(entry['url'], code=302)

if __name__ == "__main__":
    app.run(debug=True)
