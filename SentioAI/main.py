import joblib
import requests
import tempfile
from collections import Counter

def load_remote_model(url):
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        tmp_file.write(requests.get(url).content)
        return joblib.load(tmp_file.name)

model = joblib.load("model_sentioAI.pkl")
vectorizer = joblib.load("vectorizer_sentioAI.pkl")
print('loaded')

# Exemple
nouvelle_phrase = input("Donne ta phrase : ")

from preprocessing import preprocess

tokens = preprocess(nouvelle_phrase)
print("Tokens :", tokens)
vecteur = vectorizer.transform([Counter(tokens)])
prediction = int(model.predict(vecteur)[0])
if prediction == 0:
    prediction_finale = "négative"
else:
    prediction_finale = "positive"

print("Classe prédite :", prediction_finale)
