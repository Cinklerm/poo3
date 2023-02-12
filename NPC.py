from abc import ABC
from random import randint

# La classe NPC. On utilise python AbstractBaseClass
class NPC():

    # On recoit comme le parameter les valeurs que ne sont pas calcules
    def __init__(self,  nom, race, espece, point_vie, profession):
        self.force = self.rouler_des()
        self.agilite = self.rouler_des()
        self.constitution = self.rouler_des()
        self.intelligence = self.rouler_des()
        self.sagesse = self.rouler_des()
        self.charisme = self.rouler_des()
        self.classe_armure = self.rouler_des()

        self.nom = nom
        self.race = race
        self.espece = espece
        self.point_vie = point_vie
        self.profession = profession

    # Imprimer tous les champs
    def afficher_caracteristiques(self):
        print("nom:" + self.nom)
        print("race:" + self.race)
        print("espece:" + self.espece)
        print("point_vie:" + str(self.point_vie))
        print("profession:" + self.profession)
        print("classe_armure:" + str(self.classe_armure))
        print("force:" + str(self.force))
        print("agilite:" + str(self.agilite))
        print("constitution:" + str(self.constitution))
        print("intelligence:" + str(self.intelligence))
        print("sagesse:" + str(self.sagesse))
        print("charisme:" + str(self.charisme))


    # On jette le des 4 fois, et on somme le 3 plus grands
    def rouler_des(self):
        des = []
        for b in range(0, 4):
            des.append(randint(1, 6))
        des.sort(reverse=True)
        somme = des[0] + des[1] + des[2]
        return somme

# La classe pour Kobold. Elle n'a pas rien de specifique, alors on appele la classe NPC
class Kobold(NPC):
    def __init__(self, nom, race, espece, point_vie, profession):
        NPC.__init__(self,  nom, race, espece, point_vie, profession)

    def subir_dommage(self, quantite_domage):
        self.point_vie = self.point_vie - quantite_domage

# La classe pour Heros. Elle n'a pas rien de specifique, alors on appele la classe NPC
class Heros(NPC):
    def __init__(self, nom, race, espece, point_vie, profession):
        NPC.__init__(self,  nom, race, espece, point_vie, profession)

    # Comment faire override de methode.
    # https://www.educative.io/answers/how-to-do-method-overriding-in-python
    def attaquer(self, cible: Kobold):
        ''' La methode pour attaquer, version du Hero. '''
        # On jete la de avec 20 faces
        val_attaque = randint(1, 20)
        print("hero attaque:" + str(val_attaque))
        print("armour cible:" + str(cible.classe_armure))
        # Le cas d'attaque critique
        if val_attaque == 20:
            quantite_dommage = randint(1, 8)
            print("dommage:" + str(quantite_dommage))
            cible.subir_dommage(quantite_dommage)
        # Attaque rate
        elif val_attaque > 1 and val_attaque < 20:
            # Attaque normale
            if val_attaque >= cible.classe_armure:
                # on calcule le dommage
                quantite_dommage = randint(1, 6)
                print("dommage:" + str(quantite_dommage))
                cible.subir_dommage(quantite_dommage)


