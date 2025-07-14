import pandas as pd
from datasets import load_dataset
import os


def load_my_dataset():
    """"
    Télécharge les donnés et les convertis et les enregistres en CSV si ce n'est pas déja fait
    """
    if not bool(os.listdir("/Users/gabrieljeanvermeille/PycharmProjects/SentioAI/data")):
        print('Téléchargement en court...')
        dataset = load_dataset("tblard/allocine")
        print('Création des CSV')
        dataset["train"].to_pandas().to_csv("/Users/gabrieljeanvermeille/PycharmProjects/SentioAI/data/train.csv", index=False)
        dataset["validation"].to_pandas().to_csv("/Users/gabrieljeanvermeille/PycharmProjects/SentioAI/data/val.csv", index=False)
        dataset["test"].to_pandas().to_csv("/Users/gabrieljeanvermeille/PycharmProjects/SentioAI/data/test.csv", index=False)


def load_allocine_dataframe_from_csv(data_dir="data"):
    """
    Charge les fichiers .csv d'Allociné en DataFrame pandas.
    """
    train_path = os.path.join(data_dir, "train.csv")
    val_path = os.path.join(data_dir, "val.csv")
    test_path = os.path.join(data_dir, "test.csv")

    train_df = pd.read_csv(train_path)
    val_df = pd.read_csv(val_path)
    test_df = pd.read_csv(test_path)

    return train_df, val_df, test_df


if __name__ == "__main__":
    load_my_dataset()