class UserProfile:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def create_profile(self, name, age, height, weight, gender, contact_info):
        user_id = self.db_manager.add_user(name, age, height, weight, gender, contact_info)
        return user_id

    def get_profile(self, user_id):
        return self.db_manager.get_user(user_id)

    def update_profile(self, user_id, **kwargs):
        # Implement update logic
        pass
