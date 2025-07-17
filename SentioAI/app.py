from SentioAI.data_loader import load_allocine_dataframe_from_csv
from SentioAI.preprocessing import preprocess
from SentioAI.vectorizer import vectorize, creer_vocab
from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import pandas as pd
import json
import joblib

model = joblib.load("model_sentioAI.pkl")
vectorizer = joblib.load("vectorizer_sentioAI.pkl")

# Exemple
nouvelle_phrase = input("Donne ta phrase : ")

# Prétraitement (le même que tu as appliqué à ton corpus)
from SentioAI.preprocessing import preprocess

tokens = preprocess(nouvelle_phrase)
tfidf_dict = {mot: tokens.count(mot) / len(tokens) for mot in set(tokens)}
tfidf_vect = vectorizer.transform([tfidf_dict])
prediction = model.predict(tfidf_vect)

print("Classe prédite :", prediction[0])
