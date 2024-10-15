def sleep_consultation():
    return "💤 Let's improve your sleep! How many hours do you usually sleep per night? (e.g., 6, 7, 8)"

def process_sleep_response(hours):
    if hours < 6:
        return "You should aim for at least 7-8 hours of sleep each night for optimal health."
    elif 6 <= hours <= 8:
        return "Great! You're getting a good amount of sleep. Keep it up!"
    else:
        return "Too much sleep can also be a concern. Try to balance your sleep schedule."