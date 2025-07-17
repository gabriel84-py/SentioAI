import math

def creer_vocab(docs):
    """
    Construit un vocabulaire unique à partir d'une liste de documents tokenisés.

    Args:
        docs (list of list of str): Corpus sous forme d'une liste de documents,
                                    chaque document étant une liste de mots (tokens).

    Returns:
        list of str: Liste des mots uniques présents dans le corpus.
        """

    vocab_final = []
    for i in docs:
        for j in i:
            if j not in vocab_final:
                vocab_final.append(j)

    return vocab_final

def TF(docs):

    """
    Calcule TF.

    Args:
        docs (list of list of str): Corpus sous forme d'une liste de documents,
                                    chaque document étant une liste de mots (tokens).

    Returns:
        Dictionary.
        """

    TF_list = []

    for doc in docs:  # chaque doc est une liste de mots
        count = {}
        TF = {}
        length = len(doc)

        # Compter les occurrences
        for mot in doc:
            if mot in count:
                count[mot] += 1
            else:
                count[mot] = 1

        # Calcul du TF
        for mot in count:
            TF[mot] = count[mot] / length

        TF_list.append(TF)  # ajoute le dictionnaire TF de ce document à la liste

    return TF_list

def DF(docs, vocab):

    """
    Calcule TF.

    Args:
        docs (list of list of str): Corpus sous forme d'une liste de documents,
                                    chaque document étant une liste de mots (tokens).

    Returns:
        Integer.
        """
    DF = {mot: 0 for mot in vocab}
    for i in vocab:
        for h in docs:
            if i in h:
                DF[i] += 1

    return DF

def IDF(docs, vocab):
    DF_dico = DF(docs, vocab)
    N = len(docs)
    IDF_dic = {}
    for  doc in docs:
        for mot in doc:
            IDF_dic[mot] = math.log(N / DF_dico[mot])
    return IDF_dic

def Tf_Idf(docs: list, vocab):
    TF_dico = TF(docs)
    IDF_dico = IDF(docs, vocab)
    TF_IDF_list: list = []
    for idx, doc in enumerate(docs):
        TF_doc = TF_dico[idx]
        TF_IDF_doc = {}
        for mot in doc:
            TF_IDF_doc[mot] = TF_doc[mot] * IDF_dico[mot]
        TF_IDF_list.append(TF_IDF_doc)
    return TF_IDF_list

docs = [
    ["le", "chat", "mange", "la", "souris", "souris"],
    ["le", "chien", "aboie"],
    ["la", "souris", "mange", "le", "fromage"]
]
print(Tf_Idf(docs))