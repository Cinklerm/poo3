from NPC import NPC, Heros, Kobold


h = Heros(20, "martin cinkler", "ork", "homo", 50, "etudiant")
monstre = Kobold(13, "nessie", "dino", "reptile", 50, "monstre lacustre")

print("====== Hero ============")
h.afficher_caracteristiques()
print("==================")
print("======= Monstre ===========")
monstre.afficher_caracteristiques()
print("==================")
h.attaquer(monstre)
print("======== Monstre apres l'attaque ==========")
monstre.afficher_caracteristiques()
