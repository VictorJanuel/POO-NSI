from math import sqrt
from typing import Collection

class Point:
    def __init__(self, nom, x, y, z):
        self.nom = nom
        self.x = x
        self.y = y
        self.z = z
    
    def __str__(self):
        return self.nom + " : (" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + ")"

    def inf_ou_egal(self, autre_point):
        if self.x < autre_point.x:
            return True
        elif self.x == autre_point.x and self.y < autre_point.y:
            return True
        elif self.x == autre_point.x and self.y == autre_point.y and self.z < autre_point.z:
            return True
        elif self.x == autre_point.x and self.y == autre_point.y and self.z == autre_point.z:
            return True
        return False

    def distance(self, autre_point):
        return sqrt(
            (autre_point.x - self.x) ** 2 + 
            (autre_point.y - self.y) ** 2 +
            (autre_point.z - self.z) ** 2
        )

    def identique(self, autre_point):
        return self.distance(autre_point) < 0.0001


class CollectionDePoints:

    def __init__(self, nom):
        self.nom = nom
        self.liste = []

    def ajouter(self, point):
        self.liste.append(point)

    def __str__(self):
        ch = self.nom + " : ["
        for i in range(len(self.liste)):
            ch += self.liste[i].__str__()
            if i < len(self.liste) -1:
                ch += "; "
        ch += "]"
        return ch

    def appartient(self, point):
        for p in self.liste:
            if p.identique(point):
                return True
        return False

    def centre_gravite(self):
        sum_x, sum_y, sum_z = 0, 0, 0
        for p in self.liste:
            sum_x += p.x
            sum_y += p.y
            sum_z += p.z
        return Point("centre_gravite de " + self.nom,
            sum_x/len(self.liste), sum_y/len(self.liste), sum_z/len(self.liste))

    def tri(self):
        for i in range(len(self.liste)-1):
            point_min = i
            for j in range(i+1, len(self.liste)):
                if self.liste[j].inf_ou_egal(self.liste[point_min]):
                    point_min = j
            self.liste[point_min], self.liste[i] = self.liste[i], self.liste[point_min]


a = Point("A", 2.0, 3.5, 1.2)
b = Point("B", 3.0, 3.2, 1.2)
print(a.inf_ou_egal(b))
print(a.distance(b))
print(a.identique(b))

col_a = CollectionDePoints("ColA")
col_a.ajouter(a)
print(col_a)
col_a.ajouter(b)
print(col_a)

c = Point("C", 3.0, 3.1, 1.2)
d = Point("D", 1.0, 3.1, 1.0)
print(col_a.appartient(c))
print(col_a.centre_gravite())
col_a.ajouter(c)
col_a.ajouter(d)
print(col_a)
col_a.tri()
print(col_a)