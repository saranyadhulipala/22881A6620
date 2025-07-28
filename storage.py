from datetime import datetime, timedelta
from utils import current_time_plus_minutes

url_db = {}       # shortcode → {url, created, expiry}
click_log = {}    # shortcode → list of clicks

def store_url(shortcode, url, validity):
    if shortcode in url_db:
        return False, "Shortcode already exists"
    
    expiry = current_time_plus_minutes(validity)
    url_db[shortcode] = {
        "url": url,
        "created": datetime.now().isoformat(),
        "expiry": expiry
    }
    click_log[shortcode] = []
    return True, expiry

def get_url(shortcode):
    return url_db.get(shortcode)

def log_click(shortcode, request):
    click_log[shortcode].append({
        "timestamp": datetime.now().isoformat(),
        "source": request.headers.get("Referer", "unknown"),
        "ip": request.remote_addr
    })

def get_stats(shortcode):
    if shortcode not in url_db:
        return None
    return {
        "url": url_db[shortcode]['url'],
        "created": url_db[shortcode]['created'],
        "expiry": url_db[shortcode]['expiry'],
        "clicks": len(click_log.get(shortcode, [])),
        "logs": click_log.get(shortcode, [])
    }

def is_expired(expiry_iso):
    return datetime.now() > datetime.fromisoformat(expiry_iso)
