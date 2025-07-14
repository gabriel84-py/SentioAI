import pandas as pd
from datasets import load_dataset

dataset = load_dataset("tblard/allocine")
dataset["train"].to_pandas().to_csv("/Users/gabrieljeanvermeille/PycharmProjects/SentioAI/data/train.csv", index=False)
dataset["validation"].to_pandas().to_csv("/Users/gabrieljeanvermeille/PycharmProjects/SentioAI/data/val.csv", index=False)
dataset["test"].to_pandas().to_csv("/Users/gabrieljeanvermeille/PycharmProjects/SentioAI/data/test.csv", index=False)
