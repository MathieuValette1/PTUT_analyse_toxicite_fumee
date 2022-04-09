# Comment tracer n'importe quelles courbes (et plusieurs par graphes) en 5 lignes?
## Instructions:

Après importation des csv dans l'espace de travail

Utilisation de la classe TraceurCourbeAvecSeuil pour tracer des courbes:

1. Initialiser une LISTE de chemin vers un ou plusieurs fichiers CSV

2. Créer un objet traceur = TraceurCourbeAvecSeuil()

3. Set le type de mesure avec traceur.setTypeMesure(typeMesure)

4. Set le lieu s'il est unique avec traceur.set_lieu(lieu)

5. S'il y en a plusieurs, utiliser traceur.set_liste_lieu(liste_lieu)

6. Set les seuils dans une liste de seuil et se"t leur nom dans une liste de nom de seuil

7. Tracer le graph avec traceur.draw_graph()

8. OPTIONNEL:

  8.1. Set l'abscisse avec set_xlabel    Par défaut, xlabel = Temps
  
  8.2. Set l'ordonnée avec set_ylabel    Par défaut, ylabel = ug/m^3
