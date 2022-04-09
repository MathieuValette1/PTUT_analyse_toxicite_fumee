from analyses_mesures.courbes_avec_seuils_generator.TraceurCourbeAvecSeuil import TraceurCourbeAvecSeuil

mazametSaleCO2 = "../mesures/mazamet_mesures/mazametSaleCO2.csv"
mazametPropreCO2 = "../mesures/mazamet_mesures/mazametPropreCO2.csv"
mazametRemiseCO2 = "../mesures/mazamet_mesures/mazametRemiseCO2.csv"

seuils = []  # 24h, année
nom_seuils = []


def traceur_CO2_mazamet():
    # On trace les courbes

    ### CO2

    # mazamet sale PM 10
    traceur_mazametSaleCO2 = TraceurCourbeAvecSeuil([mazametSaleCO2], "CO2")
    traceur_mazametSaleCO2.setTitreGraph(
        "Evolution de la concentration des CO2 dans le vestiaire sale de mazamet")
    traceur_mazametSaleCO2.set_lieu("le vestiaire sale")
    traceur_mazametSaleCO2.set_liste_seuil(seuils)
    traceur_mazametSaleCO2.set_liste_nom_seuil(nom_seuils)
    traceur_mazametSaleCO2.set_ylabel('ppm')
    traceur_mazametSaleCO2.set_dir_path("mazamet/CO2/")
    traceur_mazametSaleCO2.set_fig_name("courbeMazametSaleCO2")
    traceur_mazametSaleCO2.draw_graph()

    # mazamet propre PM 10
    traceur_mazametPropreCO2 = TraceurCourbeAvecSeuil([mazametPropreCO2], "CO2")
    traceur_mazametPropreCO2.setTitreGraph(
        "Evolution de la concentration des CO2 dans le vestiaire propre de mazamet")
    traceur_mazametPropreCO2.set_lieu("le vestiaire propre")
    traceur_mazametPropreCO2.set_liste_seuil(seuils)
    traceur_mazametPropreCO2.set_ylabel('ppm')
    traceur_mazametPropreCO2.set_liste_nom_seuil(nom_seuils)
    traceur_mazametPropreCO2.set_dir_path("mazamet/CO2/")
    traceur_mazametPropreCO2.set_fig_name("courbeMazametPropreCO2")
    traceur_mazametPropreCO2.draw_graph()

    # mazamet remise PM 10
    traceur_mazametRemiseCO2 = TraceurCourbeAvecSeuil([mazametRemiseCO2], "CO2")
    traceur_mazametRemiseCO2.setTitreGraph("Evolution de la concentration des CO2 dans la remise de mazamet")
    traceur_mazametRemiseCO2.set_lieu("la remise")
    traceur_mazametRemiseCO2.set_liste_seuil(seuils)
    traceur_mazametRemiseCO2.set_liste_nom_seuil(nom_seuils)
    traceur_mazametRemiseCO2.set_ylabel('ppm')
    traceur_mazametRemiseCO2.set_dir_path("mazamet/CO2/")
    traceur_mazametRemiseCO2.set_fig_name("courbeMazametRemiseCO2")
    traceur_mazametRemiseCO2.draw_graph()
