#1
class StringFoo:
    def __init__(self):
        self.attribut = None

    def set_string(self, parametre):
        self.attribut = parametre

    def print_string(self):
        print(self.attribut.upper())

stringfoo = StringFoo()
stringfoo.set_string('salut')
stringfoo.print_string()

#2

class Rectangle:
    def __init__(self, largeur, longueur):
        self.largeur = largeur
        self.longueur = longueur
    def calcul_aire(self):
        return self.longueur*self.largeur

    def afficher_infos(self):
        print('longueur: ', self.longueur)
        print('largeur: ', self.largeur)
        print('Aire: ', self.calcul_aire())

rectangle = Rectangle(10, 16)
rectangle.afficher_infos()
rectangle2 = Rectangle(4,7)
rectangle2.afficher_infos()
#3
from math import pi
class Cercle:
    def __init__(self, rayon):
        self.rayon = rayon

    def calcul_aire(self):
        return self.rayon*self.rayon*pi

    def calcul_circonference(self):
        return 2*pi*self.rayon

cercle = Cercle(4)
print(cercle.calcul_aire(), cercle.calcul_circonference())
#4
class Hero:
    def __init__(self):
        self.pv = random.randint(1,10)+random.randint(1,10)
        self.force_attaque = random.randint(1,6)
        self.force_defense = random.randint(1,6)
        self.nom = nom

    def faire_une_attaque(self):
            return random.randint(1,6)+self.force_attaque

    def recevoir_dommages(self, nb_dommages):
            self.pv -= (nb_dommages-self.force_defense):












            