from Plateau import Plateau
from Terrain import Terrain

class Partie:

    def __init__(self, liste_joueur):
        self.liste_joueur = liste_joueur
        self.plateau = Plateau()

    def __str__(self):
        ch = "Les joueurs sont :\n"
        for j in self.liste_joueur:
            ch += "- " + j.nom + "\n"
        return ch

    def avoir_joueur_avec_nom(self, nom):
        for j in self.liste_joueur:
            if j.nom == nom:
                return j

    def choix_action(self, joueur):
        choix = 0
        while choix != 1:
            print("Que voulez-vous faire ?")
            print("1 - Tirer le dé")
            print("2 - Consulter mon compte")
            print("3 - Voir sur quelle case je suis")

            choix = int(input("Mon choix : "))
        
            if choix == 2:
                print(f"{joueur.nom} a sur son compte {joueur.compte}")
                print()
            elif choix == 3:
                x = joueur.position[0]
                y = joueur.position[1]
                print(f"{joueur.nom} est sur la case : {self.plateau.avoir_terrain_i_j(x,y).nom}")
                print()


    def deplacement(self, joueur):
        print(f"{joueur.nom} tire le dé")
        valeur_de = joueur.tirer_de()
        print(f"{joueur.nom} a fait {str(valeur_de)}")
        print(f"{joueur.nom} se déplace de {str(valeur_de)} case(s)")
        joueur.deplacement(valeur_de)
        
        x = joueur.position[0]
        y = joueur.position[1]
        case_joueur = self.plateau.avoir_terrain_i_j(x, y)
        print(f"{joueur.nom} est arrivé sur la case {case_joueur.nom}")
        return case_joueur


    def traitement_post_deplacement(self, joueur, case):
        if isinstance(case, Terrain):
            if case.est_achetable(): #la case n'a un propriétaire
                print(f"{case.nom} n'a pas de propriétaire")
                if joueur.compte >= case.cout_achat: #le joueur peut acheter la case
                    print(f"{case.nom} coûte {case.cout_achat} et {joueur.nom} a {joueur.compte}")
                    achat = int(input("Voulez-vous l'acheter (1/0) ? "))
                    if achat == 1: #le joueur achete la case
                        joueur.acheter(case)
                        print(f"{joueur.nom} a acheté {case.nom}")
                else: #le joueur ne peut pas acheter la case
                    print(f"Malheuresement {joueur.nom} ne peut pas acheter {case.nom}")
            else: #la case a un propriétaire
                if case.proprietaire == joueur.nom:
                    print(f"{joueur.nom} est arrivé sur une case lui appartement")
                    case.ameliorer_case(joueur)
                else:
                    print(f"La case {case.nom} a un propriétaire : {case.proprietaire}")
                    print(f"{joueur.nom} paye {case.loyer} a {case.proprietaire}")
                    joueur.payer(case, self.avoir_joueur_avec_nom(case.proprietaire))

        else:
            print(f"La case {case.nom} ne peut pas être achetée")


    def tour(self, joueur):
        print(f"Tour de {joueur.nom}")
        print()
        
        self.choix_action(joueur)
        case_joueur = self.deplacement(joueur)
        self.traitement_post_deplacement(joueur, case_joueur)

        print(f"{joueur}")
        print()

    def joueur_faillite(self):
        for j in self.liste_joueur:
            if j.compte < 0:
                return True
        return False

    def prochain_joueur(self, indice_joueur_actuel):
        if indice_joueur_actuel == len(self.liste_joueur)-1:
            return 0
        return indice_joueur_actuel + 1

    def definir_gagnant(self):
        max = 0
        j_save = ""
        for j in self.liste_joueur:
            if j.compte > max:
                max = j.compte
                j_save = j.nom
        return j_save
