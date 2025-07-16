from SentioAI.data_loader import load_allocine_dataframe_from_csv
from SentioAI.preprocessing import preprocess

train_df, val_df, test_df = load_allocine_dataframe_from_csv()

print(train_df["review"].iloc[0])
print(preprocess(train_df["review"].iloc[0]))