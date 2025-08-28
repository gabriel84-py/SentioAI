import joblib
import requests
import tempfile

def load_remote_model(url):
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        tmp_file.write(requests.get(url).content)
        return joblib.load(tmp_file.name)

model = load_remote_model("https://drive.google.com/file/d/10Yc4T0BtEUGRmPL9tvG_KDRg3ErQuAO2/view?usp=drive_link")
vectorizer = load_remote_model("https://drive.google.com/file/d/1DBsgTHD6_aW4XChtuWsF0D8um6_EN29U/view?usp=drive_link")
print('loaded')

# Exemple
nouvelle_phrase = input("Donne ta phrase : ")

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
