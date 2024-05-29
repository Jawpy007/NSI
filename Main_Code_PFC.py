import socket

def Transcription(ListeCoup: list) -> list:
    Convertisseur = {"Pierre": 0, 'Feuille': 1, "Ciseau": 2}
    return [Convertisseur[ListeCoup[0]], Convertisseur[ListeCoup[1]]]

def Winner(ValeurCoup: list) -> str:
    ValeurCoup = Transcription(ValeurCoup)
    Discriminant = (ValeurCoup[0] - ValeurCoup[1] + 3) % 3
    Gagnant = "Joueur1" if Discriminant == 1 else "Joueur2" if Discriminant == 2 else "egalite"
    return Gagnant

hostname = "127.0.0.1"
port = 56789

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((hostname, port))
s.listen(5)

print("Server is listening...")

while True:
    print("Waiting for Player 1...")
    clientsocket1, address1 = s.accept()
    print(f"Player 1 connected from {address1}")
    clientsocket1.send(bytes("Waiting for Player 2...", "utf-8"))

    print("Waiting for Player 2...")
    clientsocket2, address2 = s.accept()
    print(f"Player 2 connected from {address2}")
    clientsocket2.send(bytes("Player 2 connected. Starting the game...", "utf-8"))
    clientsocket1.send(bytes("Player 2 connected. Starting the game...", "utf-8"))

    # Informer les joueurs qu'ils peuvent jouer
    clientsocket1.send(bytes("Welcome to the server! Choose your move", "utf-8"))
    clientsocket2.send(bytes("Welcome to the server! Choose your move", "utf-8"))

    # Entrée des coups des joueurs
    MooveClient1 = clientsocket1.recv(1024).decode("utf-8")
    print(f"Player 1 chose: {MooveClient1}")
    MooveClient2 = clientsocket2.recv(1024).decode("utf-8")
    print(f"Player 2 chose: {MooveClient2}")

    # Déterminer le gagnant
    Gagnant = Winner([MooveClient1, MooveClient2])
    print(f"Winner: {Gagnant}")

    # Envoyer le résultat aux joueurs
    if Gagnant == "Joueur1":
        clientsocket1.send(bytes("Gg you win", "utf-8"))
        clientsocket2.send(bytes("Sad you lose", "utf-8"))
    elif Gagnant == "Joueur2":
        clientsocket1.send(bytes("Sad you lose", "utf-8"))
        clientsocket2.send(bytes("Gg you win", "utf-8"))
    else:
        clientsocket1.send(bytes("No winner, it's a draw", "utf-8"))
        clientsocket2.send(bytes("No winner, it's a draw", "utf-8"))

    # Fermer les connexions
    clientsocket1.close()
    clientsocket2.close()
