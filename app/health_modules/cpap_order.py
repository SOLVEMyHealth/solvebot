def cpap_info():
    return "😴 CPAP machines can greatly improve sleep quality for those with sleep apnea. We currently offer the following models:\n1. ResMed AirSense 10\n2. Philips DreamStation\n3. Fisher & Paykel SleepStyle\nWhich would you like more information about?"

def process_cpap_choice(choice):
    cpap_info = {
        "1": "The ResMed AirSense 10 is known for its quiet operation and advanced comfort features.",
        "2": "The Philips DreamStation is compact and travel-friendly with excellent humidification options.",
        "3": "The Fisher & Paykel SleepStyle offers intuitive controls and detailed sleep reports."
    }
    return cpap_info.get(choice, "I'm sorry, I don't have information about that model. Please choose 1, 2, or 3.")

def initiate_cpap_order(model):
    return f"Great choice! To order the {model}, we'll need some additional information. Would you like to proceed with the order?"
