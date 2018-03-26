import tkinter
import random
import pygame

fen = tkinter.Tk()

couleurs = ["red","blue","gold","silver"]
global choix_couleur
global bouton_couleur_boule
global song
global song_paused

choix_couleur = 0
song_paused = False

def neige(nombre_flocons):
    for i in range(0,nombre_flocons):
        x = random.randint(0,600)
        y = random.randint(0,650)
        can.create_oval(x-5, y-5, x+5, y+5, fill = "white", outline = "grey")

def tombe_neige():
    neige(3)
    fen.after(1000,tombe_neige)
    
def boule(event):
    global choix_couleur
    x = event.x
    y = event.y
##    can.create_oval(x-15, y-15, x+15, y+15, fill = couleurs[randint(0,3)], outline = "black")
    can.create_oval(x-15, y-15, x+15, y+15, fill = couleurs[choix_couleur], outline = "black")


def change_couleur():
    global choix_couleur
    global bouton_couleur_boule

    choix_couleur = choix_couleur + 1
    if choix_couleur == 4:
        choix_couleur = 0
    bouton_couleur_boule.config(bg = couleurs[choix_couleur])
    bouton_couleur_boule.pack()

def musique():
    global song_paused
    if pygame.mixer.music.get_busy() :
        print("busy")
        if song_paused :
            pygame.mixer.music.unpause()
        else:
            pygame.mixer.music.pause()
        song_paused = not song_paused
    else :
        pygame.mixer.music.play()
        song_paused = False
    
################################################################

can = tkinter.Canvas(fen, bg = "white", height = 650 , width = 600)
can.grid(row = 800 , column = 650)

sapin = tkinter.PhotoImage(file = 'SapinNoel.png', height = 0 , width = 0)
can.create_image(300, 330, image = sapin)
can.pack(side="left")

bouton_couleur_boule =  tkinter.Button(fen, text="Change de couleur de boule !!", command = change_couleur, bg = couleurs[choix_couleur])
##can.create_window(650, 600, window= bouton_couleur_boule)
bouton_couleur_boule.pack(expand=1)

bouton_neige = tkinter.Button(fen, text="Que tombe la neige !!", command = lambda: neige(10), bg = "white")
bouton_neige.pack(expand=1)

bouton_musique = tkinter.Button(fen, text="Musique noël !!", command = musique, bg = "white")
bouton_musique.pack(expand=1)

can.bind("<Button-1>",boule)
fen.after(1000,tombe_neige)
pygame.init()
##song = pygame.mixer.Sound('musique.ogg')
pygame.mixer.music.load('musique.ogg')


fen.mainloop()
