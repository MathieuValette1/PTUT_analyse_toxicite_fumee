from analyses_mesures.courbes_avec_seuils_generator.TraceurCourbeAvecSeuil import TraceurCourbeAvecSeuil

mazametSaleCOV = "../mesures/mazamet_mesures/mazametSaleCOV.csv"
mazametPropreCOV = "../mesures/mazamet_mesures/mazametPropreCOV.csv"
mazametRemiseCOV = "../mesures/mazamet_mesures/mazametRemiseCOV.csv"

seuils = [250, 500, 1000, 3000]
nom_seuils = ["Niveau 1", "Niveau 2", "Niveau 3", "Niveau 4", "Niveau 5"]

def traceur_COV_mazamet():
    # On trace les courbes

    ### COV

    # Mazamet sale PM 10
    traceur_mazametSaleCOV = TraceurCourbeAvecSeuil([mazametSaleCOV], "COV")
    traceur_mazametSaleCOV.setTitreGraph(
        "Evolution de la concentration des COV dans le vestiaire sale du 27-02 au 13-03")
    traceur_mazametSaleCOV.set_lieu("le vestiaire sale")
    traceur_mazametSaleCOV.set_liste_seuil(seuils)
    traceur_mazametSaleCOV.set_liste_nom_seuil(nom_seuils)
    traceur_mazametSaleCOV.set_dir_path("mazamet/COVt/")
    traceur_mazametSaleCOV.set_fig_name("courbeMazametSaleCOV")
    traceur_mazametSaleCOV.draw_graph()

    # Mazamet propre COV
    traceur_mazametPropreCOV = TraceurCourbeAvecSeuil([mazametPropreCOV], "COV")
    traceur_mazametPropreCOV.setTitreGraph(
        "Evolution de la concentration des COV dans le vestiaire propre du 27-02 au 13-03")
    traceur_mazametPropreCOV.set_lieu("le vestiaire propre")
    traceur_mazametPropreCOV.set_liste_seuil(seuils)
    traceur_mazametPropreCOV.set_liste_nom_seuil(nom_seuils)
    traceur_mazametPropreCOV.set_dir_path("mazamet/COVt/")
    traceur_mazametPropreCOV.set_fig_name("courbeMazametPropreCOV")
    traceur_mazametPropreCOV.draw_graph()

    # Mazamet propre COV
    traceur_mazametRemiseCOV = TraceurCourbeAvecSeuil([mazametRemiseCOV], "COV")
    traceur_mazametRemiseCOV.setTitreGraph("Evolution de la concentration des COV dans la remise du 27-02 au 13-03")
    traceur_mazametRemiseCOV.set_lieu("la remise")
    traceur_mazametRemiseCOV.set_liste_seuil(seuils)
    traceur_mazametRemiseCOV.set_liste_nom_seuil(nom_seuils)
    traceur_mazametRemiseCOV.set_dir_path("mazamet/COVt/")
    traceur_mazametRemiseCOV.set_fig_name("courbeMazametRemiseCOV")
    traceur_mazametRemiseCOV.draw_graph()
