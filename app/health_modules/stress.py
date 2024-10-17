def stress_management():
    return "🧘 Let's manage your stress. On a scale of 1-10, how would you rate your current stress level?"

def process_stress_response(level):
    level = int(level)
    if level <= 3:
        return "Your stress levels seem manageable. Keep up your good stress management practices!"
    elif 4 <= level <= 7:
        return "You're experiencing moderate stress. Try incorporating daily relaxation techniques like deep breathing or meditation. Regular exercise can also help manage stress."
    else:
        return "You're experiencing high levels of stress. It's important to address this. Consider talking to a mental health professional. In the meantime, practice stress-reduction techniques like mindfulness, exercise, and ensuring you get enough sleep."
