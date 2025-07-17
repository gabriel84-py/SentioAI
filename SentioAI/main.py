import joblib

model = joblib.load("/Users/gabrieljeanvermeille/PycharmProjects/SentioAI/SentioAI/model_sentioAI.pkl")
vectorizer = joblib.load("/Users/gabrieljeanvermeille/PycharmProjects/SentioAI/SentioAI/vectorizer_sentioAI.pkl")

# Exemple
nouvelle_phrase = input("Donne ta phrase : ")

# Prétraitement (le même que tu as appliqué à ton corpus)
from SentioAI.preprocessing import preprocess

tokens = preprocess(nouvelle_phrase)
tfidf_dict = {mot: tokens.count(mot) / len(tokens) for mot in set(tokens)}
tfidf_vect = vectorizer.transform([tfidf_dict])
prediction = model.predict(tfidf_vect)

if prediction[0] == 0:
    prediction_finale = "négative"
else:
    prediction_finale = "positive"

print("Classe prédite :", prediction_finale)
