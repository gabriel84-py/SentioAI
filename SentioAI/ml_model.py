import joblib
import csv
import os
from preprocessing import preprocess
from collections import Counter
from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LogisticRegression
import pandas as pd

def reentrainer_model():
    # Charger données originales
    df_train = pd.read_csv("/Users/gabrieljeanvermeille/PycharmProjects/SentioAI/SentioAI/data/train.csv", keep_default_na=False)

    # Charger corrections utilisateur
    if os.path.exists('/Users/gabrieljeanvermeille/PycharmProjects/SentioAI/SentioAI/data/correction.csv'):
        df_corrections = pd.read_csv("/Users/gabrieljeanvermeille/PycharmProjects/SentioAI/SentioAI/data/correction.csv", names=["texte", "label"], keep_default_na=False)
        df_train = pd.concat([df_train, df_corrections], ignore_index=True)

    # Prétraitement + vectorisation
    X = []
    y = []
    for _, row in df_train.iterrows():
        try:
            tokens = preprocess(row["review"])
        except :
            print(row["review"])
        vect = Counter(tokens)
        X.append(vect)
        y.append(row["label"])

    # Vectoriser
    new_vectorizer = DictVectorizer()
    X_vect = new_vectorizer.fit_transform(X)

    # Réentraîner
    new_model = LogisticRegression(max_iter=1000)
    new_model.fit(X_vect, y)

    # Sauvegarder
    joblib.dump(new_model, "/Users/gabrieljeanvermeille/PycharmProjects/SentioAI/SentioAI/model_sentioAI.pkl")
    joblib.dump(new_vectorizer, "/Users/gabrieljeanvermeille/PycharmProjects/SentioAI/SentioAI/vectorizer_sentioAI.pkl")

    return new_model, new_vectorizer

reentrainer_model()