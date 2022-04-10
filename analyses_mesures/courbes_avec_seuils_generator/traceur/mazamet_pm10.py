from analyses_mesures.courbes_avec_seuils_generator.TraceurCourbeAvecSeuil import TraceurCourbeAvecSeuil

mazametSalePM10 = "../mesures/mazamet_mesures/mazametSalePM10.csv"
mazametProprePM10 = "../mesures/mazamet_mesures/mazametProprePM10.csv"
mazametRemisePM10 = "../mesures/mazamet_mesures/mazametRemisePM10.csv"

op_mazamet = "../mesures/op_mazamet.xlsx"

seuils = [45, 15]  # 24h, année
nom_seuils = ["seuil 24h", "seuil année"]


def traceur_pm10_mazamet():
    # On trace les courbes

    ### PM10

    # Mazamet sale PM 10
    traceur_mazametSalePM10 = TraceurCourbeAvecSeuil([mazametSalePM10], "PM10")
    traceur_mazametSalePM10.set_op_mazamet(op_mazamet)
    traceur_mazametSalePM10.setTitreGraph(
        "Evolution de la concentration des PM10 dans le vestiaire sale de mazamet")
    traceur_mazametSalePM10.set_lieu("le vestiaire sale")
    traceur_mazametSalePM10.set_liste_seuil(seuils)
    traceur_mazametSalePM10.set_liste_nom_seuil(nom_seuils)
    traceur_mazametSalePM10.set_dir_path("mazamet/pm10/")
    traceur_mazametSalePM10.set_fig_name("pm_10_sale_mazamet")
    traceur_mazametSalePM10.draw_graph()

    # Mazamet propre PM 10
    traceur_mazametProprePM10 = TraceurCourbeAvecSeuil([mazametProprePM10], "PM10")
    traceur_mazametProprePM10.setTitreGraph(
        "Evolution de la concentration des PM10 dans le vestiaire propre de mazamet")
    traceur_mazametProprePM10.set_lieu("le vestiaire sale")
    traceur_mazametProprePM10.set_op_mazamet(op_mazamet)
    traceur_mazametProprePM10.set_liste_seuil(seuils)
    traceur_mazametProprePM10.set_liste_nom_seuil(nom_seuils)
    traceur_mazametProprePM10.set_dir_path("mazamet/pm10/")
    traceur_mazametProprePM10.set_fig_name("pm_10_propre_mazamet")
    traceur_mazametProprePM10.draw_graph()

    # Mazamet propre PM 10
    traceur_mazametRemisePM10 = TraceurCourbeAvecSeuil([mazametRemisePM10], "PM10")
    traceur_mazametRemisePM10.setTitreGraph("Evolution de la concentration des PM10 dans la remise de mazamet")
    traceur_mazametRemisePM10.set_lieu("le vestiaire sale")
    traceur_mazametRemisePM10.set_op_mazamet(op_mazamet)
    traceur_mazametRemisePM10.set_liste_seuil(seuils)
    traceur_mazametRemisePM10.set_liste_nom_seuil(nom_seuils)
    traceur_mazametRemisePM10.set_dir_path("mazamet/pm10/")
    traceur_mazametRemisePM10.set_fig_name("pm_10_remise_mazamet")
    traceur_mazametRemisePM10.draw_graph()
