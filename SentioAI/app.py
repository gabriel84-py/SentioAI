from SentioAI.data_loader import load_allocine_dataframe_from_csv
from SentioAI.preprocessing import preprocess
from SentioAI.vectorizer import vectorize, creer_vocab
import json


with open("/Volumes/T7 Shield/dev_projects/data/vectorise.json", "r", encoding="utf-8") as f:
    vectorized_data = json.load(f)

