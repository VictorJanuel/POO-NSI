from random import randint

class Joueur:

    def __init__(self, nom):
        self.nom = nom
        self.compte = 1500
        self.liste_proprietes = []
        self.position = (0,0)

    def __str__(self):
        ch = self.nom + " a " + str(self.compte) + "€\nIl possède : "
        if len(self.liste_proprietes) == 0:
            ch += "rien"
        else:
            for propriete in self.liste_proprietes:
                ch += "\n - " + propriete.nom
        return ch

    def tirer_de(self):
        return randint(1, 6)

    def deplacement(self, nb_cases):
        x = self.position[0]
        y = self.position[1]
        y += nb_cases
        
        #depassement de ligne
        x += y // 7
        if x >= 4:
            x = 0
            self.compte += 200
        y = y % 7
        self.position = (x, y)

    def acheter(self, terrain): 
        #on traite avec le fait que le joueur puisse acheter le terrain
        self.compte -= terrain.cout_achat
        self.liste_proprietes.append(terrain)
        terrain.proprietaire = self.nom

    def payer(self, terrain, joueur):
        self.compte -= terrain.loyer
        joueur.compte += terrain.loyer
