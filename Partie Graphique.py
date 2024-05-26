import socket
from tkinter import *

message = ""
msg = None
Connected = False

def connection():
    global msg, Connected
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((socket.gethostname(), 56789))
        msg = s.recv(1024)
        if msg:
            print(msg.decode("utf-8"))
            message = msg.decode("utf-8")
            # texte
            ecriture = message 
            # narrateur
            Narrateur = Label(fen, text=ecriture)
            Narrateur.grid(row=1, column=3)
            s.send(bytes("Hey I'm here", "utf-8"))
            bouton_connexion["state"] = "disabled"
            bouton_pierre["state"] = "normal"
            bouton_feuille["state"] = "normal"
            bouton_ciseau["state"] = "normal"
            Connected = True
        else:
            raise Exception("No message received from server")
    finally:
        s.close()

def Pierre():
    receveur = socket.socket(type=socket.SOCK_DGRAM)
    Message = b'Pierre'
    receveur.sendto(Message, ('192.168.1.45', 56789))

def Feuille():
    receveur = socket.socket(type=socket.SOCK_DGRAM)
    Message = b'Feuille'
    receveur.sendto(Message, ('192.168.1.45', 56789))

def Ciseau():
    receveur = socket.socket(type=socket.SOCK_DGRAM)
    Message = b'Ciseau'
    receveur.sendto(Message, ('192.168.1.45', 56789))

# GUI
fen = Tk()
fen.title("jeu")

# bouton start
bouton_connexion = Button(fen, text='Start', command=connection)
bouton_connexion.grid(row=0, column=100)

# bouton feuille
bouton_feuille = Button(fen, text='Feuille', command=Feuille, state='disabled')
bouton_feuille.grid(row=3, column=2)

# bouton pierre
bouton_pierre = Button(fen, text='Pierre', command=Pierre, state='disabled')
bouton_pierre.grid(row=3, column=3)

# bouton ciseau
bouton_ciseau = Button(fen, text='Ciseau', command=Ciseau, state='disabled')
bouton_ciseau.grid(row=3, column=4)

fen.mainloop()
