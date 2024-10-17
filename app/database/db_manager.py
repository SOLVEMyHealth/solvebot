from prisma import Prisma

class DatabaseManager:
    def __init__(self):
        self.db = Prisma()

    async def connect(self):
        await self.db.connect()

    async def disconnect(self):
        await self.db.disconnect()

    async def add_user(self, name, age, height, weight, gender, contact_info):
        user = await self.db.userprofile.create({
            'data': {
                'name': name,
                'age': age,
                'height': height,
                'weight': weight,
                'gender': gender,
                'contactInfo': contact_info
            }
        })
        return user.id

    async def get_user(self, user_id):
        return await self.db.userprofile.find_unique(where={'id': user_id})

    async def add_health_assessment(self, user_id, score, notes):
        assessment = await self.db.healthassessment.create({
            'data': {
                'userId': user_id,
                'score': score,
                'notes': notes
            }
        })
        return assessment.id

    async def add_consultation_record(self, user_id, doctor, notes):
        record = await self.db.consultationrecord.create({
            'data': {
                'userId': user_id,
                'doctor': doctor,
                'notes': notes
            }
        })
        return record.id
