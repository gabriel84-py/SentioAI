from datasets import load_dataset

def load_allocine_dataset():
    """Charge le dataset Allociné via Hugging Face."""
    dataset = load_dataset("tblard/allocine")
    return dataset["train"], dataset["validation"], dataset["test"]
