import math
from collections import Counter

def creer_vocab(docs, min_df=5, max_df_ratio=0.9):
    """
        Construit un vocabulaire limité basé sur les fréquences documentaires.
        """
    N = len(docs)
    df_counter = Counter()

    for doc in docs:
        unique_mots = set(doc)
        for mot in unique_mots:
            df_counter[mot] += 1

    vocab = [
        mot for mot, df in df_counter.items()
        if df >= min_df and df <= max_df_ratio * N
    ]

    return sorted(vocab)

def TF(docs):
    """
       Calcule la fréquence des mots (TF) pour chaque document.
    """
    print("TF commence")
    TF_list = []
    for doc in docs:
        count = Counter(doc)
        length = len(doc)
        tf_doc = {mot: count[mot] / length for mot in count}
        TF_list.append(tf_doc)
    print("TF finit")
    return TF_list

def DF(docs, vocab):
    """
        Calcule le Document Frequency (DF) pour chaque mot du vocabulaire.
    """
    print("DF commence")
    DF = {mot: 0 for mot in vocab}
    for doc in docs:
        unique_mots = set(doc)
        for mot in unique_mots:
            if mot in DF:
                DF[mot] += 1
    print("DF finit")
    return DF

def IDF(docs, vocab):
    """
        Calcule l'Inverse Document Frequency (IDF) pour chaque mot.
    """
    print("IDF commence")
    N = len(docs)
    DF_dico = DF(docs, vocab)
    IDF_dic = {}
    for mot in vocab:
        if DF_dico[mot] > 0:
            IDF_dic[mot] = math.log(N / DF_dico[mot])
        else:
            IDF_dic[mot] = 0.0
    print("IDF finit")
    return IDF_dic

def vectorize(docs: list, vocab):
    """
       Transforme une liste de documents en représentation TF-IDF vectorisée.

       Returns:
           list of list of floats: Vecteurs TF-IDF complets pour chaque document.
    """
    print('vectorize commence')
    TF_list = TF(docs)
    IDF_dic = IDF(docs, vocab)

    vecteurs = []
    for idx, doc_tf in enumerate(TF_list):
        vecteur = {}
        for mot in doc_tf:
            if mot in IDF_dic:
                vecteur[mot] = doc_tf[mot] * IDF_dic[mot]
        vecteurs.append(vecteur)  # <=== Ceci doit être dans la boucle

    print("vectorize finit")
    return vecteurs

