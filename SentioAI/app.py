from flask import Flask, render_template, request
import joblib
import csv
from preprocessing import preprocess
from collections import Counter
import os
import joblib
import requests
import tempfile

def load_remote_model(url):
    response = requests.get(url)
    response.raise_for_status()  # Pour détecter erreurs HTTP

    with tempfile.NamedTemporaryFile(suffix=".pkl") as tmp_file:
        tmp_file.write(response.content)
        tmp_file.flush()
        model = joblib.load(tmp_file.name)
    
    return model


model = joblib.load("model_sentioAI.pkl")
vectorizer = joblib.load("vectorizer_sentioAI.pkl")


app = Flask(__name__)

CORRECTION_FILE = "data/correction.csv"


@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    texte = ""

    if request.method == "POST":
        texte = request.form["texte_utilisateur"]
        print(texte, flush=True)
        if "feedback" in request.form:
            # Traitement du retour utilisateur
            correction = request.form.get("correction")
            label_corrige = request.form.get("label_corrige")
            if correction == "0":
                with open('data/correction.csv', "a", newline="", encoding="utf-8") as f:
                    writer = csv.writer(f)
                    writer.writerow([texte, label_corrige])
            return render_template("index.html", prediction=prediction, texte=texte)

        # Traitement de l’analyse initiale
        tokens = preprocess(texte)
        print("Tokens :", tokens)
        vecteur = vectorizer.transform([Counter(tokens)])
        prediction = int(model.predict(vecteur)[0])
        print(prediction)

    return render_template("index.html", prediction=prediction, texte=texte)


if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port='5000')
