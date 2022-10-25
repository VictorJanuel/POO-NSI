from Joueur import Joueur
from Plateau import Plateau
from Partie import Partie

from random import randint

if __name__ == "__main__":

    partie = Partie([Joueur("Victor"), Joueur("Yoann")])

    indice_joueur = randint(0, len(partie.liste_joueur)-1)

    while not partie.joueur_faillite():
        partie.tour(partie.liste_joueur[indice_joueur])
        indice_joueur = partie.prochain_joueur(indice_joueur)

    print(f"Le gagnant de la partie est {partie.definir_gagnant()}")


