import socket
#import librairie
from tkinter import *
#le code de jaouen
#Variable Globals
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
    Narrateur.grid(row=0, column=3)

def Pierre():
    if Connected:
        s.send(bytes("Pierre", "utf-8"))
        Result()


def Feuille():
    if Connected:
        s.send(bytes("Feuille", "utf-8"))
        Result()


def Ciseau():
    if Connected:
        s.send(bytes("Ciseau", "utf-8"))
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


#Esthetique des boutons
esthetique = {
    'font': ('Tahoma', 10, 'bold'),

    'fg': 'black',         # Couleur du texte
    'activebackground': '#FFFFFF',  # Couleur de fond quand le bouton est cliqué
    'activeforeground': 'black',    # Couleur du texte quand le bouton est cliqué
    'bd': 1,               # Bordure
    'relief': 'solid',    # Style de bordure
    'width': 5,          # Largeur du bouton en pixels
    'height': 2           # Hauteur du bouton en pixels
}


esthetique2= {
    'font': ('Verdana', 15 ,'bold')
}

esthetique3= {
    'font': ('Verdana', 10 ,'bold')
}
#fond d'écran




#bouton feuille
bouton_feuille=Button(fen,text='feuille', command=Feuille, **esthetique, state='disabled')
bouton_feuille.grid(row=1, column=1, padx=10, pady=10, sticky='e')

#bouton pierre
bouton_pierre=Button(fen,text='pierre',command=Pierre, **esthetique, state='disabled')
bouton_pierre.grid(row=1, column=2, padx=10, pady=10)

#bouton ciseau
bouton_ciseau=Button(fen,text='ciseau', command=Ciseau, **esthetique, state='disabled')
bouton_ciseau.grid(row=1, column=3, padx=10, pady=10, sticky='w')

#texte
ecriture='infos du serveur:' #changer pour mettre la réponse du joueur via le serveur

#bouton start
bouton_connexion=Button(fen, text='Recherche de match', command=connection)
bouton_connexion.grid(row=0, column=16)

#narrateur
Narrateur=Label(fen, text=ecriture, **esthetique2)
Narrateur.grid(row=0, column=0)

#infos pour echap
infech=Label(fen, text='appuyez sur echap pour quitter le mode plein écran', ** esthetique3)
infech.grid(row=4, column=15)

fen.grid_rowconfigure(0, weight=1)
fen.grid_rowconfigure(1, weight=1)
fen.grid_rowconfigure(2, weight=1)
fen.grid_columnconfigure(0, weight=1)
fen.grid_columnconfigure(1, weight=1)
fen.grid_columnconfigure(2, weight=1)



fen.mainloop()