import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from transformers import pipeline
import warnings

warnings.filterwarnings("ignore")

# Download required NLTK data
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')


class NLPEngine:
    """
    Handles emotion detection, safety keyword detection, and session emotion analysis.
    """
    
    def __init__(self):
        """Initialize the emotion classifier and preprocessing tools."""
        self.emotion_classifier = pipeline(
            "text-classification",
            model="bhadresh-savani/distilbert-base-uncased-emotion",
            framework="pt"  # Use PyTorch
        )
        
        self.stemmer = PorterStemmer()
        self.stop_words = set(stopwords.words('english'))
        
        # Crisis/escalation keywords mapped by severity
        self.crisis_keywords = {
            "critical": [
                "suicide", "kill myself", "hang myself", "end it all",
                "overdose", "cut myself", "harm myself", "slit wrist",
                "noose", "jump", "hopeless", "worthless", "burden"
            ],
            "severe": [
                "self-harm", "self harm", "hurt myself", "pain",
                "can't take it", "dark thoughts", "dying", "dead inside",
                "no reason to live", "give up", "helpless", "trapped"
            ],
            "moderate": [
                "anxious", "panic", "terrified", "overwhelmed",
                "broken", "devastated", "depressed", "numb",
                "empty", "lost", "confused", "scared"
            ]
        }
        
        # Emotion to emoji and color mapping
        self.emotion_map = {
            "sadness": {"emoji": "😢", "color": "#4A90E2"},
            "joy": {"emoji": "😊", "color": "#52D273"},
            "anger": {"emoji": "😠", "color": "#FF5252"},
            "fear": {"emoji": "😰", "color": "#FFB84D"},
            "surprise": {"emoji": "😲", "color": "#FF6B6B"},
            "love": {"emoji": "💖", "color": "#FF69B4"},
            "neutral": {"emoji": "😐", "color": "#95A5A6"}
        }
    
    def detect_emotion(self, text: str) -> dict:
        """
        Detect emotion from user input using Hugging Face transformer.
        Returns: {"emotion": str, "score": float, "emoji": str, "color": str}
        """
        try:
            result = self.emotion_classifier(text, top_k=1)
            emotion = result[0]['label'].lower()
            score = result[0]['score']
            
            emoji = self.emotion_map.get(emotion, {}).get("emoji", "🤔")
            color = self.emotion_map.get(emotion, {}).get("color", "#95A5A6")
            
            return {
                "emotion": emotion,
                "score": score,
                "emoji": emoji,
                "color": color
            }
        except Exception as e:
            print(f"Error in emotion detection: {e}")
            return {"emotion": "neutral", "score": 0.0, "emoji": "🤔", "color": "#95A5A6"}
    
    def preprocess_text(self, text: str) -> list:
        """
        Preprocess text: tokenize, lowercase, remove stopwords, stem.
        Returns: list of processed tokens
        """
        text = text.lower()
        tokens = word_tokenize(text)
        processed = [
            self.stemmer.stem(token) 
            for token in tokens 
            if token.isalnum() and token not in self.stop_words
        ]
        return processed
    
    def detect_crisis_keywords(self, text: str) -> dict:
        """
        Detect crisis or escalation keywords in user input.
        Returns: {"severity": str or None, "keywords_found": list, "is_crisis": bool}
        """
        processed_tokens = self.preprocess_text(text)
        text_lower = text.lower()
        
        severity_found = None
        keywords_found = []
        
        for severity, keywords in self.crisis_keywords.items():
            for keyword in keywords:
                if keyword in text_lower or any(
                    self.stemmer.stem(word) == self.stemmer.stem(keyword.split()[0])
                    for word in processed_tokens
                ):
                    keywords_found.append(keyword)
                    if severity_found is None:
                        severity_found = severity
                    elif severity == "critical":
                        severity_found = "critical"
        
        is_crisis = severity_found is not None
        
        return {
            "severity": severity_found,
            "keywords_found": keywords_found,
            "is_crisis": is_crisis
        }
    
    def calculate_session_emotion(self, session_emotions: list) -> dict:
        """
        Calculate dominant emotion from last 5 interactions.
        Returns: {"dominant_emotion": str, "trend": str, "emoji": str, "color": str}
        """
        if not session_emotions:
            return {
                "dominant_emotion": "neutral",
                "trend": "starting",
                "emoji": "🤔",
                "color": "#95A5A6"
            }
        
        emotion_counts = {}
        for emotion_data in session_emotions:
            emotion = emotion_data.get("emotion", "neutral")
            emotion_counts[emotion] = emotion_counts.get(emotion, 0) + 1
        
        dominant_emotion = max(emotion_counts, key=emotion_counts.get)
        
        # Determine trend
        if len(session_emotions) >= 2:
            last_emotion = session_emotions[-1].get("emotion", "neutral")
            if last_emotion == "joy" or last_emotion == "love":
                trend = "improving"
            elif last_emotion in ["sadness", "fear", "anger"]:
                trend = "declining"
            else:
                trend = "stable"
        else:
            trend = "starting"
        
        emoji = self.emotion_map.get(dominant_emotion, {}).get("emoji", "🤔")
        color = self.emotion_map.get(dominant_emotion, {}).get("color", "#95A5A6")
        
        return {
            "dominant_emotion": dominant_emotion,
            "trend": trend,
            "emoji": emoji,
            "color": color
        }
    
    def get_emotion_history_for_chart(self, session_emotions: list) -> list:
        """
        Convert session emotions to chart data.
        Returns: list of dicts with index and emotion for charting
        """
        return [
            {
                "interaction": i + 1,
                "emotion": data.get("emotion", "neutral"),
                "score": data.get("score", 0.5)
            }
            for i, data in enumerate(session_emotions[-10:])
        ]
