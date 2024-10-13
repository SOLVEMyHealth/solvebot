from app.health_modules import sleep, nutrition , exercise , stress, sexual_health , health_assessment
from app.services import appointment_scheduler , cpap_order
from app.bot.natural_language_processor import process_natural_language
from app.bot.user_profile import UserProfile 


class SolveMyHealth: 
    def __init__(self , db_manager):
        self.db_manager= db_manager
        self.user_profile = UserProfile(db_manager)
    
    def handle_user_input(self, user_input):
        intent = process_natural_language(user_input)

        if intent == 'sleep':
            return sleep.sleep_consultation()
        elif intent == 'nutrition':
            return nutrition.nutrition_advice()
        elif intent == 'exercise':
            return exercise.exercise_guidance()
        elif intent == 'stress':
            return sexual_health.sexual_health_consultation()
        elif intent == 'appointment':
            return appointment_scheduler.book_appointment()
        elif intent == 'cpap':
            return cpap_order.cpap_info()
        elif intent == 'health_assessment':
            return health_assessment.start_assessment()
        else: 
            return "I m sorry i didnt get that , Please try again."
        

        
         