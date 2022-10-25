class Terrain:

    def __init__(self, nom, couleur):
        self.nom = nom
        self.couleur = couleur
        self.nb_maison = 0
        self.nb_hotel = 0
        self.proprietaire = ""

        if self.couleur == "marron":
            self.cout_achat = 60
            self.loyer = 40
            self.cout_ajout_maison = 100
            self.cout_ajout_hotel = 500
        elif self.couleur == "bleu":
            self.cout_achat = 100
            self.loyer = 80
            self.cout_ajout_maison = 100
            self.cout_ajout_hotel = 500
        elif self.couleur == "rose":
            self.cout_achat = 140
            self.loyer = 120
            self.cout_ajout_maison = 150
            self.cout_ajout_hotel = 700
        elif self.couleur == "orange":
            self.cout_achat = 180
            self.loyer = 160
            self.cout_ajout_maison = 150
            self.cout_ajout_hotel = 700
        elif self.couleur == "rouge":
            self.cout_achat = 220
            self.loyer = 200
            self.cout_ajout_maison = 200
            self.cout_ajout_hotel = 900
        elif self.couleur == "jaune":
            self.cout_achat = 260
            self.loyer = 240
            self.cout_ajout_maison = 200
            self.cout_ajout_hotel = 900
        elif self.couleur == "vert":
            self.cout_achat = 300
            self.loyer = 280
            self.cout_ajout_maison = 300
            self.cout_ajout_hotel = 950
        elif self.couleur == "violet":
            self.cout_achat = 350
            self.loyer = 330
            self.cout_ajout_maison = 350
            self.cout_ajout_hotel = 1000

    def __str__(self):
        ch = self.nom + "\n"
        ch += "loyer : " + str(self.loyer) + "\n"
        ch += "prix avec 1 maison : " + str(round(self.loyer * 1.2)) + "\n"
        ch += "prix avec 2 maisons : " + str(round((self.loyer * 1.2) *1.2))  + "\n"
        ch += "prix avec 3 maisons : " + str(round(((self.loyer * 1.2) *1.2) *1.2))  + "\n"
        ch += "prix avec 4 maisons : " + str(round((((self.loyer * 1.2) *1.2) *1.2) *1.2))  + "\n"
        ch += "prix avec 1 hotel : " + str(round(((((self.loyer * 1.2) *1.2) *1.2) *1.2) *1.4))  + "\n"
        ch += "coût d'1 maison : " + str(self.cout_ajout_maison) + "\n"
        ch += "coût d'1 hotel : " + str(self.cout_ajout_hotel) + "\n"
        ch += "prix d'achat : " + str(self.cout_achat) + "\n"
        ch += "propriétaire : " + str(self.proprietaire) + "\n"
        return ch

    def est_achetable(self):
        return self.proprietaire == ""

    def ameliorer_case(self, joueur):
        if self.nb_maison < 4:
            if joueur.compte - self.cout_ajout_maison >= 0:
                print(f"{joueur.nom} peut améliorer {self.nom} en mettant une maison pour {self.cout_ajout_maison}€")
                print(f"Le prix de la case passera de {self.loyer} a {self.loyer * 1.2}")

                choix = int(input("Améliorer la case (1/0) ? "))
                if choix == 1:
                    self.nb_maison += 1
                    joueur.compte -= self.cout_ajout_maison
                    self.loyer *= 1.2
        elif self.nb_maison == 4:
            if joueur.compte - self.cout_ajout_hotel >= 0:
                print(f"{joueur.nom} peut améliorer {self.nom} en mettant un hotel pour {self.cout_ajout_hotel}€")
                print(f"Le prix de la case passera de {self.loyer} a {self.loyer * 1.4}")

                choix = int(input("Améliorer la case (1/0) ? "))
                if choix == 1:
                    self.nb_hotel += 1
                    joueur.compte -= self.cout_ajout_hotel
                    self.loyer *= 1.4
        else:
            print(f"{self.nom} ne peut pas être amélioré")




