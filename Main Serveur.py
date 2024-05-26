#Script Server

import socket,os
Tick = 0
Players = {}
hostname=socket.gethostname()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 56789))
s.listen(5)

while True:
    clientsocket, address = s.accept()
    print(f"Connection from {address} complete")
    clientsocket.send(bytes("Welcome to the server!","utf-8"))
    MessageClient = clientsocket.recv(1024)
    print(MessageClient.decode("utf-8"))
    
    clientsocket2, address2 = s.accept()
    print(f"Connection with player 2 from {address2} complete")
    clientsocket2.send(bytes("Welcome to the server!","utf-8"))
    MessageClient2 = clientsocket2.recv(1024)
    print(MessageClient2.decode("utf-8"))
    
    clientsocket.send(bytes("Game is starting! Choose ur moove","utf-8"))
    clientsocket2.send(bytes("Game is starting! Choose ur moove","utf-8"))


""" 
    print(donnee, adress)
    adressIp = adress[0]
    #Setup Players and Game start
    if donnee == b'Connect' and Tick <- 1:
        Players[Tick] = adressIp
        Tick + 1
        print (Players)
        Verification = TwoPlayer (Players)
    else:
        if Verification == True:
            Message = b"start"
        class Joueur1:
            Numero = 1
            Adresse = Players[0]
            Start = server.sendto((Message),(Adresse, 56789))
        class Joueur2:
            Numero = 2
            Adresse = Players[1]
            Start = server.sendto( (Message),(Adresse,56789))
"""