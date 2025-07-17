from SentioAI.data_loader import load_allocine_dataframe_from_csv
from SentioAI.preprocessing import preprocess

train_df, val_df, test_df = load_allocine_dataframe_from_csv()

def format_df(df):
    docs = []
    for ligne in df["review"]:
        tokens = preprocess(ligne)
        docs.append(tokens)