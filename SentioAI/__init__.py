# sentioai/__init__.py

# Importations internes
from .preprocessing import clean_text, preprocess_texts
from .vectorizer import load_vectorizer, vectorize_texts
from .ml_model import SentimentClassifier
from .deep_model import SentioLSTM

# Optionnel : message de confirmation
print("📦 SentioAI package loaded.")
