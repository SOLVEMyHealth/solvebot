def exercise_guidance():
    return "🏋️ Let's get you moving! How often do you currently exercise per week? (e.g., 0-1 times, 2-3 times, 4+ times)"

def process_exercise_response(frequency):
    if "0-1" in frequency:
        return "Start small! Aim for 3 30-minute sessions per week. Try brisk walking, swimming, or cycling. Remember to warm up and cool down."
    elif "2-3" in frequency:
        return "Great start! Try to increase to 4-5 sessions per week. Mix cardio with strength training for best results."
    else:
        return "Excellent! Keep up the good work. Make sure you're including both cardio and strength training in your routine. Don't forget rest days for recovery."
