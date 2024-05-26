#Script Server

import socket,os
Tick = 0
Players = {}
hostname="127.0.0.1"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("127.0.0.1", 56789))
s.listen(5)

def Transcription(ListeCoup: list) -> list:
    Convertisseur: dict = {"Pierre":0,'Feuille':1,"Ciseau":2}
    return [Convertisseur[ListeCoup[0]],Convertisseur[ListeCoup[1]]]


def Winner(ValeurCoup: list) -> str:
    ValeurCoup: int = Transcription(ValeurCoup)
    Discriminant: int = (ValeurCoup[0]-ValeurCoup[1]+3)%3

    Gagnant = "Joueur1" if Discriminant==1 else "Joueur2" if Discriminant== 2 else "egalite"

    return Gagnant

while True:
    clientsocket, address = s.accept()
    print(f"Connection from {address} complete")
    clientsocket.send(bytes("Welcome to the server! Choose ur moove","utf-8"))
    MessageClient = clientsocket.recv(1024)
    print(MessageClient.decode("utf-8"))

    clientsocket2, address2 = s.accept()
    print(f"Connection with player 2 from {address2} complete")
    clientsocket2.send(bytes("Welcome to the server! Choose ur moove","utf-8"))
    MessageClient2 = clientsocket2.recv(1024)
    print(MessageClient2.decode("utf-8"))

    MooveClient1 = clientsocket.recv(1024)
    MooveJ1= MooveClient1.decode("utf-8")
    print(MooveJ1)
    MooveClient2 = clientsocket2.recv(1024)
    MooveJ2 = MooveClient2.decode("utf-8")
    print(MooveJ2)

    Gagnant = Winner([MooveJ1,MooveJ2])
    print(Gagnant)


    if Gagnant == "Joueur1":
        clientsocket.send(bytes("Gg u win","utf-8"))
        clientsocket2.send(bytes("Sad u loose","utf-8"))

    elif Gagnant == "Joueur2":
        clientsocket.send(bytes("Sad u loose","utf-8"))
        clientsocket2.send(bytes("Gg u win","utf-8"))

    else:
        clientsocket.send(bytes("No winner Draw","utf-8"))
        clientsocket2.send(bytes("No winner Draw","utf-8"))
