from analyses_mesures.courbes_avec_seuils_generator.TraceurCourbeAvecSeuil import TraceurCourbeAvecSeuil

mazametSalePM1 = "../mesures/mazamet_mesures/mazametSalePM1.csv"
mazametProprePM1 = "../mesures/mazamet_mesures/mazametProprePM1.csv"
mazametRemisePM1 = "../mesures/mazamet_mesures/mazametRemisePM1.csv"
op_mazamet = "../mesures/op_mazamet.xlsx"

seuils = []


def traceur_pm1_mazamet():
    # On trace les courbes

    ### PM1

    # Mazamet sale PM 1
    traceur_mazametSalePM1 = TraceurCourbeAvecSeuil([mazametSalePM1], "PM1")
    traceur_mazametSalePM1.setTitreGraph(
        "Evolution de la concentration des PM1 dans le vestiaire sale de mazamet")
    traceur_mazametSalePM1.set_lieu("le vestiaire sale")
    traceur_mazametSalePM1.set_liste_seuil(seuils)
    traceur_mazametSalePM1.set_liste_nom_seuil([])
    traceur_mazametSalePM1.set_op_mazamet(op_mazamet)
    traceur_mazametSalePM1.set_dir_path("mazamet/pm1/")
    traceur_mazametSalePM1.set_fig_name("courbeMazametSalePM1")
    traceur_mazametSalePM1.draw_graph()

    # Mazamet propre PM 1
    traceur_mazametProprePM1 = TraceurCourbeAvecSeuil([mazametProprePM1], "PM1")
    traceur_mazametProprePM1.setTitreGraph(
        "Evolution de la concentration des PM1 dans le vestiaire propre de mazamet")
    traceur_mazametProprePM1.set_lieu("le vestiaire sale")
    traceur_mazametProprePM1.set_liste_seuil(seuils)
    traceur_mazametProprePM1.set_liste_nom_seuil([])
    traceur_mazametProprePM1.set_op_mazamet(op_mazamet)
    traceur_mazametProprePM1.set_dir_path("mazamet/pm1/")
    traceur_mazametProprePM1.set_fig_name("courbeMazametProprePM1")
    traceur_mazametProprePM1.draw_graph()

    # Mazamet propre PM 1
    traceur_mazametRemisePM1 = TraceurCourbeAvecSeuil([mazametRemisePM1], "PM1")
    traceur_mazametRemisePM1.setTitreGraph("Evolution de la concentration des PM1 dans la remise de mazamet")
    traceur_mazametRemisePM1.set_lieu("la remise")
    traceur_mazametRemisePM1.set_liste_seuil(seuils)
    traceur_mazametRemisePM1.set_op_mazamet(op_mazamet)
    traceur_mazametRemisePM1.set_liste_nom_seuil([])
    traceur_mazametRemisePM1.set_dir_path("mazamet/pm1/")
    traceur_mazametRemisePM1.set_fig_name("courbeMazametRemisePM1")
    traceur_mazametRemisePM1.draw_graph()
