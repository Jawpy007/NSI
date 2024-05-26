def Transcription(ListeCoup: list) -> list:
    Convertisseur: dict = {"Pierre":0,'Papier':1,"Ciseau":2}
    return [Convertisseur[ListeCoup[0]],Convertisseur[ListeCoup[1]]]


def Winner(ValeurCoup: list) -> str:
    ValeurCoup: int = Transcription(ValeurCoup)
    Discriminant: int = (ValeurCoup[0]-ValeurCoup[1]+3)%3
    
    Gagnant = "Joueur1" if Discriminant==1 else "Joueur2" if Discriminant== 2 else "égalité"
    
    return Gagnant

