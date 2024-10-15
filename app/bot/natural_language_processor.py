import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

nltk.download('punkt')
nltk.download('stopwords')

def process_natural_language(user_input):
    # Tokenize the input
    tokens = word_tokenize(user_input.lower())
    
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [word for word in tokens if word not in stop_words]
    
    # Simple keyword matching for intent recognition
    intents = {
        'sleep': ['sleep', 'insomnia', 'tired'],
        'nutrition': ['food', 'diet', 'nutrition', 'eat'],
        'exercise': ['exercise', 'workout', 'fitness'],
        'stress': ['stress', 'anxiety', 'relax'],
        'sexual_health': ['sexual', 'sex', 'std'],
        'appointment': ['appointment', 'book', 'schedule'],
        'cpap': ['cpap', 'sleep apnea'],
        'health_assessment': ['assessment', 'check', 'evaluate']
    }
    
    for intent, keywords in intents.items():
        if any(keyword in filtered_tokens for keyword in keywords):
            return intent
    
    return 'unknown'