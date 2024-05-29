import socket
import threading
from tkinter import *

# Variables Globales
s = None
message = ""
msg = None
Connected = False

def connection():
    global msg, Connected, s
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect(("127.0.0.1", 56789))
        msg = s.recv(1024)
        if msg:
            print(msg.decode("utf-8"))
            message = msg.decode("utf-8")
            # texte
            ecriture = message
            # narrateur
            Narrateur.config(text=ecriture)


            if "Waiting player 2" in message:
                threading.Thread(target=WaitingGame).start()
            else:
                enable_buttons()
                Connected = True
        else:
            raise Exception("No message received from server")
    except Exception as e:
        print(f"Connection failed: {e}")

def enable_buttons():
    bouton_connexion["state"] = "disabled"
    bouton_pierre["state"] = "normal"
    bouton_feuille["state"] = "normal"
    bouton_ciseau["state"] = "normal"

def WaitingGame():
    global s, Connected
    while True:
        msg = s.recv(1024)
        if msg:
            message = msg.decode("utf-8")
            if "Player 2 connected. Starting the game..." in message:
                # Texte
                ecriture = message
                # Narrateur
                Narrateur.config(text=ecriture)
                enable_buttons()
                Connected = True
                break
            else:
                ecriture = message
                Narrateur.config(text=ecriture)

def WaitingResult():
    Confirmation = s.recv(1024)
    if "Can Play" in Confirmation.decode("utf-8"):
        msg = s.recv(1024)
        Resultat = msg.decode("utf-8")
        Narrateur.config(text=Resultat)
    else:
        print("Test")

def Result():
    Confirmation = s.recv(1024)
    if "Waiting The other Player" in Confirmation.decode("utf-8"):
        threading.Thread(target=WaitingResult).start()
    else:
        msg = s.recv(1024)
        Resultat = msg.decode("utf-8")
        Narrateur.config(text=Resultat)

def Pierre():
    if Connected:
        threading.Thread(target=send_choice, args=("Pierre",)).start()

def Feuille():
    if Connected:
        threading.Thread(target=send_choice, args=("Feuille",)).start()

def Ciseau():
    if Connected:
        threading.Thread(target=send_choice, args=("Ciseau",)).start()

def send_choice(choice):
    s.send(bytes(choice, "utf-8"))
    Result()

def exit_fullscreen(event=None):
    """Quitter le mode plein écran."""
    fen.attributes("-fullscreen", False)
    return "break"

# GUI
fen = Tk()
fen.title("jeu")
fen.attributes('-fullscreen', True)
fen.bind('<Escape>', exit_fullscreen)

# Esthétique des boutons
esthetique = {
    'font': ('Tahoma', 10, 'bold'),
    'fg': 'black',
    'activebackground': '#FFFFFF',
    'activeforeground': 'black',
    'bd': 1,
    'relief': 'solid',
    'width': 5,
    'height': 2
}

esthetique2 = {'font': ('Verdana', 15, 'bold')}
esthetique3 = {'font': ('Verdana', 10, 'bold')}

# Bouton feuille
bouton_feuille = Button(fen, text='feuille', command=Feuille, **esthetique, state='disabled')
bouton_feuille.grid(row=1, column=1, padx=10, pady=10, sticky='e')

# Bouton pierre
bouton_pierre = Button(fen, text='pierre', command=Pierre, **esthetique, state='disabled')
bouton_pierre.grid(row=1, column=2, padx=10, pady=10)

# Bouton ciseau
bouton_ciseau = Button(fen, text='ciseau', command=Ciseau, **esthetique, state='disabled')
bouton_ciseau.grid(row=1, column=3, padx=10, pady=10, sticky='w')

# Texte
ecriture = 'infos du serveur:'

# Bouton start
bouton_connexion = Button(fen, text='Recherche de match', command=connection)
bouton_connexion.grid(row=0, column=16)

# Narrateur
Narrateur = Label(fen, text=ecriture, **esthetique2)
Narrateur.grid(row=0, column=0)

# Infos pour échapper
infech = Label(fen, text='appuyez sur echap pour quitter le mode plein écran', **esthetique3)
infech.grid(row=4, column=15)

fen.grid_rowconfigure(0, weight=1)
fen.grid_rowconfigure(1, weight=1)
fen.grid_rowconfigure(2, weight=1)
fen.grid_columnconfigure(0, weight=1)
fen.grid_columnconfigure(1, weight=1)
fen.grid_columnconfigure(2, weight=1)

fen.mainloop()
