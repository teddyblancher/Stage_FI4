#machine_a_sous

"""
Bibliotheques utilisees dans le programme
"""


import os
from random import randrange

"""
Variables globales utilisees dans le programme
"""

#argent definie les moyens du joueur, ses gains, et s'il a la possibilite de continuer la partie.
argent = 1000
#mise definie la quantite d'argent mis en jeu par le joueur.
mise = 0
#continuer_partie permet au joueur d'arreter s'il le veut ou s'il n'a plus d'argent.
continuer_partie = False

"""
Variables propre au programme
"""

#carac_roue correspond à l'apparence des roues de la roulette, (chaque roue a les meme caracteres mais pas disposé dans le meme ordre (indice)).
carac_roue1 = ["0", "7", "X", "*", "-", "+", "^", "$" ,"#",]
carac_roue2 = ["0", "X", "-", "^", "#", "7", "*", "+", "$",]
carac_roue3 = ["7", "*", "+", "$", "0", "X", "-", "^", "#",]
  
#X,Y,Z permettent d'obtenir l'indice correspondant a un caractere de la roue    
X = randrange(9)
Y = randrange(9)
Z = randrange(9)

#initialisation de liste de dimension 3 pour creer les roues (A correspond a la roue 1). Si on initialise pas on ne peut pas les remplir.
A = [0,0,0]
B = [0,0,0]
C = [0,0,0]

#vainqueur permet d'identifier quand le joueur gagne ou perd
vainqueur = False

"""
Debut du programme machine_a_sous
"""

print ("Bienvenue au machine a sous vous avez ", argent, "$.")


#lancement de la machine a sous il
i=0
while i < 3:
    A[i] = carac_roue1[(X+i)%9]
    i += 1

j=0
while j < 3:
    B[j] = carac_roue2[(Y+j)%9]
    j += 1

k=0
while k < 3:
    C[k] = carac_roue3[(Z+k)%9]
    k += 1


#affichage du resultat de la machine a sous
print(A[0],"|",B[0],"|",C[0])
print("---------")
print(A[1],"|",B[1],"|",C[1])
print("---------")
print(A[2],"|",B[2],"|",C[2])

#determine si le joueur gagne et quel est le montant de ses gains/pertes
l=0
while l<3:
    if "A[l]"=="B[l]"=="C[l]":
      
        gain += mise*15
        vainqueur = True
        """print ("Le montant de votre porte monnaie s'eleve a", argent, "$.")""""
    elif  "A[0]"=="B[1]"=="C[2]" or "A[2]"=="B[1]"=="C[0]":
       gain += mise *15
       vainqueur = True
    l+=1
if vainqueur= True:
    argent+= gain
    print ("Felicitation vous avez gagne(e)", gain, "$. Votre argent est donc de ", argent, "$.")
else:
    agrent -= mise
    print ("Dommage vous avez perdu(e)", mise, "$. Votre argent est donc de ", argent, "$.")
