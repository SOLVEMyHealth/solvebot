from app.health_modules import sleep, nutrition, exercise, stress, sexual_health, health_assessment

class SolveMyHealthBot:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    async def handle_user_input(self, user_input):
        # This is a simplified version. You'll need to implement proper state management
        # and conversation flow in a real application.
        if 'sleep' in user_input.lower():
            return await sleep.sleep_consultation()
        elif 'nutrition' in user_input.lower():
            return await nutrition.nutrition_advice()
        elif 'exercise' in user_input.lower():
            return await exercise.exercise_guidance()
        elif 'stress' in user_input.lower():
            return await stress.stress_management()
        elif 'sexual health' in user_input.lower():
            return await sexual_health.sexual_health_consultation()
        elif 'health assessment' in user_input.lower():
            return await health_assessment.start_assessment()
        else:
            return "I'm not sure how to help with that. Can you try rephrasing your question?"

    async def create_user_profile(self, name, age, height, weight, gender, contact_info):
        user_id = await self.db_manager.add_user(name, age, height, weight, gender, contact_info)
        return f"User profile created with ID: {user_id}"

    async def get_user_profile(self, user_id):
        user = await self.db_manager.get_user(user_id)
        if user:
            return f"User: {user.name}, Age: {user.age}, Height: {user.height}, Weight: {user.weight}"
        else:
            return "User not found"
