#Script Server
import socket,os
Tick = 0
Players = {}
hostname=socket.gethostname()

#Check if Two player are connect
Verification = False
def Twoplayer (Liste):
    if len(Liste) == 2:
        return True
    return False


while True:
    server = socket.socket(type=socket.SOCK_DGRAM)
    server.bind((hostname, 56789))
    donnee, adress = server. recvfrom(1500)
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