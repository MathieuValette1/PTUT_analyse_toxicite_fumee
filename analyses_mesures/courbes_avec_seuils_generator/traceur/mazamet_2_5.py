from analyses_mesures.courbes_avec_seuils_generator.TraceurCourbeAvecSeuil import TraceurCourbeAvecSeuil

mazametSalePM2_5 = "../mesures/mazamet_mesures/mazametSalePM2_5.csv"
mazametProprePM2_5 = "../mesures/mazamet_mesures/mazametProprePM2_5.csv"
mazametRemisePM2_5 = "../mesures/mazamet_mesures/mazametRemisePM2_5.csv"

seuils = [15,5] # 24h année

def traceur_pm2_5_mazamet():


    # On trace les courbes

    ### PM2_5

    # Mazamet sale PM 2_5
    traceur_mazametSalePM2_5 = TraceurCourbeAvecSeuil([mazametSalePM2_5], "PM2_5")
    traceur_mazametSalePM2_5.setTitreGraph(
        "Evolution de la concentration des PM2_5 dans le vestiaire sale du 27-02 au 13-03")
    traceur_mazametSalePM2_5.set_lieu("le vestiaire sale")
    traceur_mazametSalePM2_5.set_liste_seuil(seuils)
    traceur_mazametSalePM2_5.set_liste_nom_seuil(["seuil 24h", "seuil année"])
    traceur_mazametSalePM2_5.set_dir_path("mazamet/pm2_5/")
    traceur_mazametSalePM2_5.set_fig_name("courbeMazametSalePM2_5")
    traceur_mazametSalePM2_5.draw_graph()

    # Mazamet propre PM 2_5
    traceur_mazametProprePM2_5 = TraceurCourbeAvecSeuil([mazametProprePM2_5], "PM2_5")
    traceur_mazametProprePM2_5.setTitreGraph(
        "Evolution de la concentration des PM2_5 dans le vestiaire propre de mazamet")
    traceur_mazametProprePM2_5.set_lieu("le vestiaire propre")
    traceur_mazametProprePM2_5.set_liste_seuil(seuils)
    traceur_mazametProprePM2_5.set_liste_nom_seuil(["seuil 24h", "seuil année"])
    traceur_mazametProprePM2_5.set_dir_path("mazamet/pm2_5/")
    traceur_mazametProprePM2_5.set_fig_name("courbeMazametProprePM2_5")
    traceur_mazametProprePM2_5.draw_graph()

    # Mazamet propre PM 2_5
    traceur_mazametRemisePM2_5 = TraceurCourbeAvecSeuil([mazametRemisePM2_5], "PM2_5")
    traceur_mazametRemisePM2_5.setTitreGraph("Evolution de la concentration des PM2_5 dans la remise de mazamet")
    traceur_mazametRemisePM2_5.set_lieu("la remise")
    traceur_mazametRemisePM2_5.set_liste_seuil(seuils)
    traceur_mazametRemisePM2_5.set_liste_nom_seuil(["seuil 24h", "seuil année"])
    traceur_mazametRemisePM2_5.set_dir_path("mazamet/pm2_5/")
    traceur_mazametRemisePM2_5.set_fig_name("courbeMazametRemisePM2_5")
    traceur_mazametRemisePM2_5.draw_graph()
