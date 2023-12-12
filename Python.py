import csv
import matplotlib.pyplot as plt
table = []

with open('RTE_2020.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        # Vérifiez si la ligne contient au moins une cellule non vide
        if any(cell.strip() for cell in row):
            # Ajoutez la ligne au tableau
            table.append(row)
# Imprimez le tableau
for row in table:
    print(row)

# Partie Calcule de colonne:

# Indice de la colonne à calculer
indice_colonne_a_calculer = 7
# Initialiser la variable pour stocker la somme
somme_colonne = 0

# Parcourir le tableau et calculer la somme de la colonne spécifiée
for row in table:
    try:
        valeur_colonne = float(row[indice_colonne_a_calculer])
        somme_colonne += valeur_colonne
    except ValueError:
        None
    Fioul = somme_colonne
# Afficher le résultat
print(f"La somme de la colonne Fioul est : {Fioul} MW.")

indice_colonne_a_calculer = 8
somme_colonne = 0

for row in table:
    try:
        valeur_colonne = float(row[indice_colonne_a_calculer])
        somme_colonne += valeur_colonne
    except ValueError:
        None
    Charbon = somme_colonne
print(f"La somme de la colonne charbon est : {somme_colonne} MW.")

indice_colonne_a_calculer = 9
somme_colonne = 0

for row in table:
    try:
        valeur_colonne = float(row[indice_colonne_a_calculer])
        somme_colonne += valeur_colonne
    except ValueError:
        None
    Gaz = somme_colonne
print(f"La somme de la colonne gaz est : {somme_colonne} MW.")

indice_colonne_a_calculer = 10
somme_colonne = 0

for row in table:
    try:
        valeur_colonne = float(row[indice_colonne_a_calculer])
        somme_colonne += valeur_colonne
    except ValueError:
        None
    Nucleaire = somme_colonne
print(f"La somme de la colonne nucleaire est : {somme_colonne} MW.")

indice_colonne_a_calculer = 11
somme_colonne = 0

for row in table:
    try:
        valeur_colonne = float(row[indice_colonne_a_calculer])
        somme_colonne += valeur_colonne
    except ValueError:
        None
    Eolien = somme_colonne
print(f"La somme de la colonne éolien est : {somme_colonne} MW.")

indice_colonne_a_calculer = 12
somme_colonne = 0

for row in table:
    try:
        valeur_colonne = float(row[indice_colonne_a_calculer])
        somme_colonne += valeur_colonne
    except ValueError:
        None
    Solaire = somme_colonne
print(f"La somme de la colonne solaire est : {somme_colonne} MW.")

indice_colonne_a_calculer = 13
somme_colonne = 0

for row in table:
    try:
        valeur_colonne = float(row[indice_colonne_a_calculer])
        somme_colonne += valeur_colonne
    except ValueError:
        None
    Hydraulique = somme_colonne
print(f"La somme de la colonne Hydraulique est : {somme_colonne} MW.")

indice_colonne_a_calculer = 15
somme_colonne = 0

for row in table:
    try:
        valeur_colonne = float(row[indice_colonne_a_calculer])
        somme_colonne += valeur_colonne
    except ValueError:
        None
    Bioenergies = somme_colonne
print(f"La somme de la colonne bioenergies est : {somme_colonne} MW.")


# Partie Diagramme:
labels = 'Solaire', 'Gaz', 'Charbon', 'Nucleaire','Eolien','Fioul','Hydraulique','Bioenergies'
sizes = [ Solaire, Gaz, Charbon, Nucleaire ,Eolien , Fioul, Hydraulique, Bioenergies]
colors = ['gold', 'darkgray', 'gray', 'lightgreen', 'lightblue', 'lightgray', 'blue', 'green']
explode = (0, 0.2 , 0, 0, 0, 0, 0, 0)

plt.figure(figsize=(10, 10))

plt.pie(sizes, explode=explode, labels=labels, colors=colors, 
        autopct='%1.1f%%', shadow=False, startangle=90)

plt.axis('equal')

plt.savefig('Diagrame de production d_énergie.png')
plt.tight_layout()
plt.show()