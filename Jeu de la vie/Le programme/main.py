import pygame, math, random, sys
from pygame.locals import *

from constantes import *
from World import *
from Cell import *

#JEU DE LA VIE de Mathis Techer Tle E

pygame.time.set_timer(USEREVENT, 200)
"""Pour faire simple, cette fonction va mettre un timer de 200 milisecondes à chaque evenements
C'est un truc de pygame mais ca me sert juste pour a boucle"""

w = World(nb_case_x,nb_case_y) #j'initalise la class World à w
w.init() #j'utilise la methode init de la class World

pause = True #pour savoir si le jeu est en pause ou pas

while True: #la boucle de gameplay
	#EVENTS
	for event in pygame.event.get(): #je regarde tous les évenements de pygame
		if event.type == QUIT: #si la fenetre se ferme
			pygame.quit() #alors je fermer proprement la fenetre (pour eviter les grosses erreurs)
			sys.exit()

		if event.type == KEYDOWN: #les évenements claviers
			if event.key == K_ESCAPE: #si la touche echape est pressé
				pygame.quit() #je quitte le jeu
				sys.exit()
			if event.key == K_RIGHT: #si je presse la touche fleche de droite
				w.calcule(False) #je calcule l'etat de toutes les cellules
				w.calculeVoisine() #je calcule le nombre de voisines
			if event.key == K_LEFT:#si la flèche gauche est pressé
				w.calcule(True)
				w.calculeVoisine()
			if event.key == K_p: #si p est pressé
				pause = not pause #j'inverse l'état du booléen pause

		if event.type == MOUSEBUTTONDOWN: #les évenements souris
			mX = event.pos[0] #j'actualise la posistion x de la souris
			mY = event.pos[1] #j'actualise la position y de la souris
			if event.button == 1:
				w.surimi(mX,mY,CONF)
			if event.button == 4: #si la mollette vers le haut
				if ACTUAL_CONF+1 > len(CONF_LIST)-1: #je verfiie que je ne dépasse pas la taille de la liste
					ACTUAL_CONF = 0 #si oui alors on reviens au début
				else: #sinon
					ACTUAL_CONF = ACTUAL_CONF + 1 #on augmente de 1
				CONF = CONF_LIST[ACTUAL_CONF] #CONF est égale à l'élément dans CONF_LIST
				TEMPS_FONT2 = 50
			if event.button == 5: #si la mollette vers le bas
				if ACTUAL_CONF-1 < 0: #je regarde qu'on ne sort pas de la liste
					ACTUAL_CONF = len(CONF_LIST) - 1 #si oui alors on reprend au dernier élement de la liste
				else: #sinon
					ACTUAL_CONF = ACTUAL_CONF - 1 #on retranche de 1 élement
				CONF = CONF_LIST[ACTUAL_CONF]
				TEMPS_FONT2 = 50
			if event.button == 3: #si le bouton droit de la souris est pressé
				if 0<=mX<=tile_size*nb_case_x and 0<=mY<=tile_size*nb_case_y:
					"""que la pos de la souris est bien dans la feuille
					qu'elle ne dépasse pas du nombre de cases*leurs tailles"""
					if w.listCells[int(mX/tile_size)][int(mY/tile_size)].state == 1: #dans le doc
						w.listCells[int(mX/tile_size)][int(mY/tile_size)].state = 0
					else:
						w.listCells[int(mX/tile_size)][int(mY/tile_size)].state = 1
					w.calculeVoisine() #je calcule le nombre de vosines

		if pause == False: #si on est pas en pause
			if event.type == USEREVENT: #je calule le tout (le nombre de voisines + l'état)
				w.calcule(False)
				w.calculeVoisine()

	fps_label = font1.render("FPS: {:.2F}".format(clock.get_fps()), True, ROUGE) #je définit un affichage des FPS en bas à droite en rouge
	fps_rect = fps_label.get_rect(bottomright = TAILLEFENETRE) #je définit un rect (la 'hitbox' de cet affichage)
	CONF_label = font2.render(CONF, True, VERT, NOIR) #je créer un affichage texte de CONF avec le font2 (taille de 32)
	CONF_rect = CONF_label.get_rect(center = (960,90)) #je créer une hitbox en 960,90

	#REBLIT
	fenetre.fill(BLANC) #je remplis le fond de la feuille de blanc

	w.draw(fenetre, pause) #je dessine toutes les lignes

	TEMPS_FONT2 = TEMPS_FONT2 - 1
	if not TEMPS_FONT2 < 0:
		fenetre.blit(CONF_label, CONF_rect) #j'affiche les textes sur la fenetre
	fenetre.blit(fps_label, fps_rect)


	#REFRESH
	pygame.display.flip() #j'actualise la fenetre
	clock.tick(FPS) #la fenetre tournera au nombre de FPS définit
