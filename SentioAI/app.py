from flask import Flask, render_template, request
import joblib
from preprocessing import preprocess  # Ton propre module de prétraitement
from collections import Counter

# Initialisation de l'application Flask
app = Flask(__name__)

# Chargement du modèle et du vectorizer
model = joblib.load("model_sentioAI.pkl")
vectorizer = joblib.load("vectorizer_sentioAI.pkl")

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    if request.method == "POST":
        texte = request.form["texte_utilisateur"]
        tokens = preprocess(texte)
        tokens_count = Counter(tokens)
        vecteur = vectorizer.transform([tokens_count])
        prediction = model.predict(vecteur)[0]
        print("PRÉDICTION :", prediction)
    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port='5000')
