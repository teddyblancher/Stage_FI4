# Jeu de roulette simulé
import os
from random import randrange
from math import ceil
from donnees import *

#Déclaration des variables initiales

print ("Bienvenue à la table de roulette, vous avez", argent, "$.")

while continuer_partie: # Tant que l'on oit continuer la partie, on demande a l'utilisateur de saisir le numero sur lequel il veut miser
    numero_mise = -1 # Initialisation à (-1) de la variable "numero_mise", qui contiendra la saisie de l'utilisateur, afin de toujours valider la condition de la boucle au lancement 
    while numero_mise < 0 or numero_mise > 49:
        numero_mise = input("Sur quel numero voulez vous miser ? (entre 0 et 49)") # Demande de saisie à l'utilisateur du numero sur lequel il veut miser
        try:
            numero_mise = int(numero_mise)
        except ValueError:
            print("Vous n'avez pas ecrit un numero")
            numero_mise = -1
            
        if numero_mise < 0:
            print("Vous avez ecrit un numero inferieur a 0")
        if numero_mise > 49:
            print("Vous avez ecrit un numero superieur a 49")

    mise = 0
    while mise <= 0 or mise > argent:
        mise = input("Combien voulez vous miser ?")
        try:
            mise = int(mise)
        except ValueError:
            print("Vous n'avez pas ecrit un nombre")
            mise = 0
            continue
        if mise <= 0 :
            print("Vous avez eccrit une mise inferieure a 0")
        if mise > argent :
            print("Vous avez ecrit une mise superieure a votre porte monnaie, il vous reste", argent,"$.")

    numero_gagnant = randrange(50)
    print("La roue tourne et s'arrete sur le numero", numero_gagnant," !")

    if numero_mise == numero_gagnant:
        print("Felicitations ! Vous obtenez 3 fois votre mise :", 3*mise, "$!")
        argent += mise*3
        print ("Le montant de votre porte monnaie s'eleve a", argent, "$.")
    elif numero_mise % 2 == numero_gagnant % 2:
        mise = ceil(0.5 * mise)
        print("Vous avez mise sur la bonne couleur. Vous obtenez 50% de votre mise:", mise, "$!")
        argent += mise
        print ("Le montant de votre porte monnaie s'eleve a", argent, "$.")
    else :
        print("Dommage, mauvaise couleur et mauvais numero, tu perd ta mise")
        argent -= mise
        print ("Le montant de votre porte monnaie s'eleve a", argent, "$.")
        
    if argent <=0:
        rajout = 0
        print("Vous n'avez plus d'argent")
        argent = rajoutDeFond (rajout,argent)
        
print("Fin de partie")
