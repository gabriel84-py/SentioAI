import unicodedata


def lettre_in_liste(liste: list):
    for i in liste:
        if i.isalpha():
            return True
    return False

def tokeniser(texte):
    mot_en_court = []
    liste_de_mot = []
    for i in texte:
        if i != " " or i != "," or i != ";":
            mot_en_court.append(i)
        if i == " ":
            if len(mot_en_court) > 0:
                liste_de_mot.append("".join(mot_en_court))
                mot_en_court = []
    if lettre_in_liste(mot_en_court):
        liste_de_mot.append("".join(mot_en_court))
        mot_en_court = []

    return liste_de_mot

def enlever_accent(texte):
    texte = unicodedata.normalize('NFD', texte)
    for i in texte:
        if unicodedata.category(i) == "Mn":
            texte = texte.replace(i, "")
    return texte

def stop_words(texte: list):
    final_list = []
    stop_words_inutiles = [
        "alors", "au", "aux", "avec", "ce", "cet", "cette", "ces", "ceux", "ci", "cela",
        "dans", "de", "des", "du", "en", "et", "eux", "il", "elle", "ils", "elles",
        "je", "tu", "il", "elle", "nous", "vous", "ils", "elles", "le", "la", "les", "lui", "leur",
        "ma", "mes", "mon", "notre", "nos", "ta", "tes", "ton", "votre", "vos",
        "moi", "toi", "te", "se", "s", "t", "y", "c", "d", "l", "m", "n",
        "qu", "que", "qui", "quoi", "où", "on", "un", "une",
        "es", "est", "était", "étaient", "étant", "étions", "êtes", "sont",
        "ai", "as", "avons", "avez", "ont", "avais", "avait", "avions", "aviez", "avaient",
        "eu", "eue", "eues", "eus", "ayant",
        "ici", "là", "quel", "quelle", "quels", "quelles",
        "aucunement", "parfois", "souvent", "toujours", "rarement",
        "lorsque", "lorsqu", "depuis", "puisque", "tandis", "ainsi", "entre",
        "ceci", "cela", "ça", "comme", "autre", "autres", "chacun", "tous", "tout", "toute", "toutes"
    ]

    for i in texte:
        if i not in stop_words_inutiles:
            i.append(final_list)

    return final_list

def preprocess(texte):
    caractères_a_netoyer = list(".,?!;:\"'()[]{}@#$%^&*-_=+~/\\|<>")

    """
    Nettoie une chaîne de caractères en supprimant ponctuations et majuscules.

    Args:
        texte (str): Texte brut à nettoyer.

    Returns:
        str: Texte nettoyé.
    """

    texte_lowercase = texte.lower()
    texte_lowercase = list(texte_lowercase)
    bon = []
    for i in texte_lowercase:
        if i not in caractères_a_netoyer:
            bon.append(i)
        else:
            bon.append(" ")
    textsans_characters = "".join(bon)
    text_sans_accent = enlever_accent(textsans_characters)
    tokenise = tokeniser(text_sans_accent)
    for i in tokenise:
        if i == " ":
            tokenise.remove(i)
            if i == " ":
                tokenise.remove(i)
                if i == " ":
                    tokenise.remove(i)

    new_space = []
    for i in tokenise:
        i = list(i)
        for j in range(len(i)):
            if i[j] == ' ':
                del i[j]
        i = "".join(i)
        new_space.append(i)

    final_list = stop_words(new_space)

    return final_list