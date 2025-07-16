"""
from SentioAI.data_loader import load_allocine_dataframe_from_csv

train_df, val_df, test_df = load_allocine_dataframe_from_csv()

print(train_df[train_df["review"].str.contains("horrible.*nul|nul.*horrible", case=False)])
print(train_df['review'].iloc[2782])
"""
print(len('okay '))