import random
import string
from datetime import datetime, timedelta

def generate_shortcode(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def current_time_plus_minutes(mins):
    return (datetime.now() + timedelta(minutes=mins)).isoformat()
