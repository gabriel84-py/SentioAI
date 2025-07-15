def lettre_in_liste(liste):
    for i in liste:
        if i.isalpha():
            return True
    return False

def tokeniser(texte):
    mot_en_court = []
    liste_de_mot = []
    for i in texte:
        if i != " ":
            mot_en_court.append(i)
            print("".join(mot_en_court))
        if i == " ":
            if len(mot_en_court) > 0:
                liste_de_mot.append("".join(mot_en_court))
                mot_en_court = []
    if lettre_in_liste(mot_en_court):
        liste_de_mot.append("".join(mot_en_court))
        mot_en_court = []

    return liste_de_mot

def nettoyer(texte):
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

    textsans_characters = "".join(bon)

    tokenise = tokeniser(textsans_characters)

    return tokenise


print(nettoyer('ceci est un test'))