import pygame
from pygame.locals import *

from constantes import *
from Cell import *

class World:
	def __init__(self, nbr_x, nbr_y):
		"""
		nbr_x : nombre de cases en x
		nbr_y : nombre de cases en y
		"""
		self.nbr_x = nbr_x #le nombre de cases en x
		self.nbr_y = nbr_y #le nombre de cases en y
		self.listCells = [] #la liste des cellules (liste de liste)
		self.gen = 0 #le nombre de génération

	def init(self):
		"""
		pour initaliser la liste de cellules
		"""
		for bidule in range(self.nbr_x):
			#je crée une liste de liste pour le nombre de cases en x
			self.listCells.append([])
		for x in range(self.nbr_x):
			for y in range(self.nbr_y):
				#pour chaque cases de la liste j'ajoute une cellule
				self.listCells[x].append(Cell(x, y, 0))
		for x in range(len(self.listCells)):
			for y in range(len(self.listCells[x])):
				#pour chaque une je regarde le nombre de voisines
				self.listCells[x][y].voisine(self.listCells, self.nbr_x, self.nbr_y)



	def calcule(self, clear):
		"""
		Permet de modifier l'etat de toutes les cellules en fonction du nombre de voisines
		clear : booléen pour réinitaliser ou non les cellules
		"""
		if not clear:
			self.gen += 1 #je modifie le nombre de génération
			for x in range(len(self.listCells)):
				for y in range(len(self.listCells[x])):
					#pour chaque cellule je modifie sont etat
					self.listCells[x][y].calcule()
		else:
			self.gen = 0 #je réinitalise le nombre de génération
			for x in range(len(self.listCells)):
				for y in range(len(self.listCells[x])):
					#pour chaque cellule je modifie sont etat
					self.listCells[x][y].state = 0

	def calculeVoisine(self):
		"""
		Permet de calculer ne nombre de voisines de chaque cellules
		"""
		for x in range(len(self.listCells)):
			for y in range(len(self.listCells[x])):
				#pour chaque cellules je calcule le nombre de voisines
				self.listCells[x][y].voisine(self.listCells, self.nbr_x, self.nbr_y)

	def draw(self, fenetre, pause):
		"""
		Permet de dessiner tout ce qu'il y a sur la feuille, les cellules, les lignes
		fenetre : la fenetre du jeu
		pause : si le jeu est en pause ou pas
		"""
		for x in range(len(self.listCells)):
			for y in range(len(self.listCells[x])):
				#pour chaque cellule je dessine la case
				self.listCells[x][y].draw(fenetre)

		#je définit un texte pour afficher si on est en pause ou pas et le nombre de génération en rouge
		gen_label = font1.render(str(self.gen)+str(pause), True, ROUGE)
		fenetre.blit(gen_label, (0,0)) #en 0,0 (en haut à gauche)

	def surimi(self,mX,mY,CONF):
		"""
		Permet de charger une structure à partir d'un fichier texte
		mY : pos Y de la souris
		mX : pos X de la souris
		CONF : configuration de la structure

		C'était plus simple de chercher dans un fichier que de modifier manuelement chaque cellules
		"""
		f = open('Le programme/struct/' + CONF + '.txt','r') #j'ouvre le fichier
		file = f.readlines() #je le copie dans une variable 'file'
		f.close() #je ferme le fichier
		for y in range(len(file)): #je regarde pour chaque ligne
			for x in range(len(file[0])): #pour chaque case
				if not file[y][x] == '\n': #si c'est pas un retour à la ligne
					if int(mX/tile_size)+x < nb_case_x and int(mY/tile_size)+y < nb_case_y: #si on dépasse pas de la feuille
						#je modifie l'état de la cellule correspondante avec ce qui est écrit dans le fichier
						#plus de détails dans le doc
						self.listCells[int(mX/tile_size)+x][int(mY/tile_size)+y].state = int(file[y][x])
		self.calculeVoisine() #je calcul les voisines
