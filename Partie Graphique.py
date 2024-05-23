from tkinter import *
#Server receveur / envoie
import socket


def connection():
    receveur=socket.socket(type=socket.SOCK_DGRAM)
    Message = b'Connect'
    receveur.sendto(Message,('192.168.1.45',56789))
    while True:
        server = socket.socket(type=socket.SOCK_DGRAM)
        server.bind(('localhost',56789))
        donnee,adress = server.recvfrom(1500)
#Def fonction pierre / feuille / ciseau
def Pierre():
    receveur=socket.socket(type=socket.SOCK_DGRAM)
    Message = b'Pierre'
    receveur.sendto(Message,('192.168.1.45 ',56789))
   

def Feuille():
    receveur=socket.socket(type=socket.SOCK_DGRAM)
    Message = b'Feuille'
    receveur.sendto(Message,('192.168.1.45 ',56789))


def Ciseau():
    receveur=socket.socket(type=socket.SOCK_DGRAM)
    Message = b'ciseau'
    receveur.sendto(Message,('192.168.1.45 ',56789))

#GUI
fen=Tk()
fen.title("jeu")

#bouton feuille
bouton_feuille=Button(fen,text='feuille', command=Feuille)
bouton_feuille.grid(row = 3, column =2)

#bouton pierre
bouton_pierre=Button(fen,text='pierre',command=Pierre)
bouton_pierre.grid(row=3, column=3)

#bouton ciseau
bouton_ciseau=Button(fen,text='ciseau', command=Ciseau)
bouton_ciseau.grid(row=3, column=4)

#texte
ecriture='au tour de' #changer pour mettre la réponse du joueur via le serveur

#bouton start
bouton_connexion=Button(fen, text='Start', command=connection)
bouton_connexion.grid(row=0, column=100)

#narrateur
Narrateur=Label(fen, text=ecriture)
Narrateur.grid(row=1, column=3)


fen.mainloop()