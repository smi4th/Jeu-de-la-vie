import pygame
from pygame.locals import *
from constantes import *

class Cell:
	def __init__(self, x, y, state):
		self.x = x #la position en x
		self.y = y #la position en y
		self.state = state #0 morte 1 vivante
		self.nmbVoisine = 0 #le nombre de voisines

	def voisine(self, listCells, nb_x, nb_y):
		"""
		Calcul le nombre de voisines
		listCells : list de toutes les cellules
		nb_x : le nombre de cellules en x
		nb_y le nombre de cellules en y
		"""
		voisine = 0
		#d'abord (choix artistique), je regarde les cellules Est, Ouest, Nord, Sud
		if self.x+1<nb_x: #si la cellule de droite n'est pas en dehors de la taille du nombre de cellule en x
			if listCells[self.x+1][self.y].state == 1: #si la cellule à droite est a 1 (vivante)
				voisine += 1
		if 0<=self.x-1: #si la cellule de gauche n'est pas inferieur à 0, pour des raisons évidentes elle ne doit pas
			if listCells[self.x-1][self.y].state == 1: #si la cellule de gauche est à 1
				voisine += 1
		if self.y+1<nb_y: #pareil mais pour les y
			if listCells[self.x][self.y+1].state == 1:
				voisine += 1
		if 0<=self.y-1:
			if listCells[self.x][self.y-1].state == 1:
				voisine += 1

		#puis les intermédiaires, (Nord Est, Nord Ouest,...)
		if self.x+1<nb_x and self.y+1<nb_y: #du coup je fait attention a ce que l'on dépasse pas de la feuille
			if listCells[self.x+1][self.y+1].state == 1:
				voisine += 1
		if 0<=self.x-1 and self.y+1<nb_y:
			if listCells[self.x-1][self.y+1].state == 1:
				voisine += 1
		if 0<=self.x-1 and 0<=self.y-1:
			if listCells[self.x-1][self.y-1].state == 1:
				voisine += 1
		if self.x+1<nb_x and 0<=self.y-1:
			if listCells[self.x+1][self.y-1].state == 1:
				voisine += 1

		self.nmbVoisine = voisine #le nombre de voisine est actualisé

	def calcule(self):
		"""
		Permet de calculer et de modifier l'etat d'une cellule en fonction de l'attribut self.nmbVoisine

		survie si 2 ou 3 voisines
		nait si 3 voisines
		mort <2 ou >3 voisines
		"""
		if self.state == 0: #si elle  est à 0
			if self.nmbVoisine == 3: #si il y a 3 voisines
				self.state = 1 #elle nait

		if self.state == 1: #si elle est à 1
			if self.nmbVoisine < 2: #qu'il y a moins de 2 voisines
				self.state = 0 #elle meurt
			elif self.nmbVoisine == 2:
				self.state = 1
			elif self.nmbVoisine > 3:
				self.state = 0

	def draw(self, fenetre):
		"""
		Permet de dessiner sur la feuille la case et les lines qui l'entoure
		fenetre : la fenetre d'affichage
		"""
		if self.state == 0: #si elle est morte = BLANC
			pygame.draw.rect(fenetre, BLANC, (self.x * tile_size, self.y * tile_size, tile_size, tile_size), 0)
			pygame.draw.line(fenetre, GRISF, (self.x * tile_size, self.y * tile_size), (self.x * tile_size+tile_size, self.y * tile_size), 1)
			pygame.draw.line(fenetre, GRISF, (self.x * tile_size, self.y * tile_size), (self.x * tile_size, self.y * tile_size+tile_size), 1)
			pygame.draw.line(fenetre, GRISF, (self.x * tile_size, self.y * tile_size+tile_size), (self.x * tile_size+tile_size, self.y * tile_size+tile_size), 1)
			pygame.draw.line(fenetre, GRISF, (self.x * tile_size+tile_size, self.y * tile_size), (self.x * tile_size+tile_size, self.y * tile_size+tile_size), 1)
		if self.state == 1: #si elle est vivante = NOIRE
			pygame.draw.rect(fenetre, NOIR, (self.x * tile_size, self.y * tile_size, tile_size, tile_size), 0)
			pygame.draw.line(fenetre, GRISC, (self.x * tile_size, self.y * tile_size), (self.x * tile_size+tile_size, self.y * tile_size), 1)
			pygame.draw.line(fenetre, GRISC, (self.x * tile_size, self.y * tile_size), (self.x * tile_size, self.y * tile_size+tile_size), 1)
			pygame.draw.line(fenetre, GRISC, (self.x * tile_size, self.y * tile_size+tile_size), (self.x * tile_size+tile_size, self.y * tile_size+tile_size), 1)
			pygame.draw.line(fenetre, GRISC, (self.x * tile_size+tile_size, self.y * tile_size), (self.x * tile_size+tile_size, self.y * tile_size+tile_size), 1)
		"""
		Je vais détailler une ligne qui étais trop longue à détailler dans le programme
		  pygame.draw.rect(fenetre, BLANC, (self.x * tile_size, self.y * tile_size, tile_size, tile_size), 0)
		la fenetre est la fenetre de jeu
		BLANC est la couleur de la case (ici blanche car morte). BLANC est définit en RGB dans constantes.py
		(self.x * tile_size, self.y * tile_size, tile_size, tile_size) est un rect (une hitbox)
		le rect est défini en position x = self.x * tile_size
		le rect est défini en position y = self.y * tile_size
		le rect à une taille x et y de tile_size, tile_size
		le 0 permet de remplir le rect de la couleur

		  pygame.draw.line(fenetre, GRISC, (self.x * tile_size, self.y * tile_size), (self.x * tile_size+tile_size, self.y * tile_size), 1)
		permet de tracer une ligne sur la fenetre de couleur GRISC
		de x1, y1 = (self.x * tile_size, self.y * tile_size)
		à x2, y2 = (self.x * tile_size+tile_size, self.y * tile_size)
		le 1 est l'épaisseur de la ligne
		"""
