def book_appointment():
    return "📅 Let's schedule your appointment. What type of specialist would you like to see? (e.g., General Practitioner, Nutritionist, Physiotherapist)"

def process_specialist_choice(specialist):
    # In a real application, you'd check availability and offer specific time slots
    return f"Great, I can help you book an appointment with a {specialist}. What day would work best for you?"

def process_appointment_day(day):
    # Again, in a real application, you'd check actual availability
    return f"Excellent. We have openings on {day} at 10:00 AM, 2:00 PM, and 4:00 PM. Which time works best for you?"

def confirm_appointment(time):
    return f"Perfect! I've scheduled your appointment for {time}. You'll receive a confirmation email shortly with more details. Is there anything else I can help you with?"
