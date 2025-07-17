"""
from SentioAI.data_loader import load_allocine_dataframe_from_csv

train_df, val_df, test_df = load_allocine_dataframe_from_csv()

print(train_df[train_df["review"].str.contains("horrible.*nul|nul.*horrible", case=False)])
print(train_df['review'].iloc[2782])
"""
"""
docs = [
    ["le", "chat", "mange", "la", "souris", "souris"],
    ["le", "chien", "aboie"],
    ["la", "souris", "mange", "le", "fromage"]
]
TF(docs)
"""
"""
train_df, val_df, test_df = load_allocine_dataframe_from_csv()

def format_in_docs_df(df):
    X = df["review"]
    X_processed = [preprocess(texte) for texte in X]
    return X_processed

train_docs = format_in_docs_df(train_df)
val_docs = format_in_docs_df(val_df)
test_docs = format_in_docs_df(test_df)

with open("/Users/gabrieljeanvermeille/PycharmProjects/SentioAI/data/vocab.json", "r", encoding="utf-8") as f:
    all_vocab = json.load(f)

data_to_save = {
    "train": vectorize(train_docs, all_vocab),
    "val": vectorize(val_docs, all_vocab),
    "test": vectorize(test_docs, all_vocab)
}

with open("/Volumes/T7 Shield/dev_projects/data/vectorise.json", "w", encoding="utf-8") as f:
    json.dump(data_to_save, f, ensure_ascii=False, indent=4)
"""




"""

with open("/Volumes/T7 Shield/dev_projects/data/vectorise.json", "r", encoding="utf-8") as f:
    data_vectorized = json.load(f)

X_train = data_vectorized["train"]
X_val = data_vectorized["val"]
X_test = data_vectorized["test"]

# Chargement des labels
train_df = pd.read_csv("/Users/gabrieljeanvermeille/PycharmProjects/SentioAI/data/train.csv")
val_df = pd.read_csv("/Users/gabrieljeanvermeille/PycharmProjects/SentioAI/data/val.csv")
test_df = pd.read_csv("/Users/gabrieljeanvermeille/PycharmProjects/SentioAI/data/test.csv")

y_train = train_df["label"].tolist()
y_val = val_df["label"].tolist()
y_test = test_df["label"].tolist()


vectorizer = DictVectorizer(sparse=True)  # ou sparse=False si petit corpus

X_train_vect = vectorizer.fit_transform(X_train)
X_val_vect = vectorizer.transform(X_val)
X_test_vect = vectorizer.transform(X_test)

model = LogisticRegression(max_iter=1000)
model.fit(X_train_vect, y_train)

y_test_pred = model.predict(X_test_vect)
test_accuracy = accuracy_score(y_test, y_test_pred)
print("Test Accuracy:", test_accuracy)


joblib.dump(model, "/Users/gabrieljeanvermeille/PycharmProjects/SentioAI/SentioAI/model_sentioAI.pkl")
joblib.dump(vectorizer, "/Users/gabrieljeanvermeille/PycharmProjects/SentioAI/SentioAI/vectorizer_sentioAI.pkl")

"""