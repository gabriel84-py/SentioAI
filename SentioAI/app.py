from SentioAI.data_loader import load_allocine_dataframe_from_csv
from SentioAI.preprocessing import preprocess
from SentioAI.vectorizer import vectorize, creer_vocab
import json

train_df, val_df, test_df = load_allocine_dataframe_from_csv()

def format_in_docs_df(df):
    X = df["review"]
    X_processed = [preprocess(texte) for texte in X]
    return X_processed

train_docs = format_in_docs_df(train_df)
val_docs = format_in_docs_df(val_df)
test_docs = format_in_docs_df(test_df)

all_vocab = creer_vocab(train_docs)

data_to_save = {
    "train": vectorize(train_docs, all_vocab),
    "val": vectorize(val_docs, all_vocab),
    "test": vectorize(test_docs, all_vocab)
}

with open("vectorized_all.json", "w", encoding="utf-8") as f:
    json.dump(data_to_save, f, ensure_ascii=False, indent=4)

with open("vectorized_all.json", "r", encoding="utf-8") as f:
    vectorized_data = json.load(f)

train = vectorized_data["train"]
print(train)