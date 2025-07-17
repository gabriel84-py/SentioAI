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