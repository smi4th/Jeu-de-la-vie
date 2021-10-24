import pygame
from pygame.locals import *
import glob, os
from os.path import basename, splitext

"""
Ici c'est un fichier qui ressence les constantes que j'utilise
J'ai vu sur Internet cette manière de faire pour les variables et c'est assez clair je pense
ca me permet de savoir tout sur mes variables
"""

#couleur que je peut utiliser, elles sont préfaites ici au cas ou je voudrais les changer
#Elles sont faites en RGB
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
GRISF = (60 ,60, 60)
GRISC = (150 ,150, 150)
ROUGE = (255, 0, 0)
VERT = (0, 255, 0)
JAUNE = (255, 255, 0)
BLEU = (0, 0, 255)

#Les variables de la taille de la fenetre (je met du 1920*1080 car c'est la taille de mon écran)
#si la taille de votre écran n'est pas la meme le programme ne la mettera pas en plein écran
TAILLEFENETRE = (1920, 1080)
TAILLEFENETRE_X = TAILLEFENETRE[0]
TAILLEFENETRE_Y = TAILLEFENETRE[1]

tile_size = 30 #la taille en pixel d'une tuile (case)
nb_case_x = 64 #le nombre de cases en x
nb_case_y = 36 #le nombre de cases en y

ACTUAL_CONF = 0
CONF_LIST = []
for i in range(len(os.listdir('Le programme/struct'))):
    filepath = glob.glob('Le programme\struct\*.txt')[i]
    CONF_LIST.append(splitext(basename(filepath))[0])
CONF = CONF_LIST[ACTUAL_CONF]

FPS = 60 #les FPS (frames per second)

pygame.init() #j'initalise pygame de manière plus poussé
pygame.font.init() #je crée un font, ca me servira à afficher du texte
fenetre = pygame.display.set_mode(TAILLEFENETRE, FULLSCREEN) #je crée la fenetre

#texte
font1 = pygame.font.SysFont("Arial", 16) #les caractéristiques de mon texte (taille 16 et police arial)
font2 = pygame.font.SysFont("Arial", 32)
TEMPS_FONT2 = 50 #le temps en milisecondes ou le texte font2 apparait

#temps
clock = pygame.time.Clock()
