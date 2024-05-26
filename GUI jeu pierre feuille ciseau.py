import socket
from tkinter import *

#Variable Globals
s = None
message = ""
msg = None
Connected = False

def connection():
    global msg, Connected, s
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
    except Exception as e:
        print(f"Connection failed: {e}")

def Result():
    msg = s.recv(1024)
    Resultat = msg.decode("utf-8")
        # texte
    ecriture = Resultat 
    
        # narrateur
    Narrateur = Label(fen, text=ecriture)
    Narrateur.grid(row=1, column=3)
    
def Pierre():
    if Connected:
        s.send(bytes("Pierre", "utf-8"))


def Feuille():
    if Connected:
        s.send(bytes("Feuille", "utf-8"))
        

def Ciseau():
    if Connected:
        s.send(bytes("Ciseau", "utf-8"))

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

