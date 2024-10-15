def nutrition_advice():
    return "🥗 Let's talk about your nutrition! What's your main dietary goal? (e.g., weight loss, muscle gain, balanced diet)"

def process_nutrition_response(goal):
    if "weight loss" in goal.lower():
        return "For weight loss, focus on creating a calorie deficit. Eat plenty of vegetables, lean proteins, and whole grains. Limit processed foods and sugary drinks."
    elif "muscle gain" in goal.lower():
        return "To gain muscle, increase your protein intake and ensure you're eating enough calories. Focus on lean meats, fish, eggs, and plant-based proteins like beans and lentils."
    else:
        return "For a balanced diet, aim to include a variety of fruits, vegetables, whole grains, lean proteins, and healthy fats in your meals. Stay hydrated and limit processed foods."
