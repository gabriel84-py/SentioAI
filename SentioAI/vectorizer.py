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

    print(vocab_final)

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

    print(TF_list)

#creer_vocab([["hello", "holaaaa"], ["hello", "heyy"]])
