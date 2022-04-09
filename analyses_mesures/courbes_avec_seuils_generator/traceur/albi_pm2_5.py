from analyses_mesures.courbes_avec_seuils_generator.TraceurCourbeAvecSeuil import TraceurCourbeAvecSeuil

albiSalePM2_5 = "../mesures/albi_mesures/albiSalePM2_5.csv"
albiProprePM2_5 = "../mesures/albi_mesures/albiProprePM2_5.csv"
albiRemisePM2_5 = "../mesures/albi_mesures/albiRemisePM2_5.csv"

seuils = [15,5] # 24h année

def traceur_pm2_5_albi():


    # On trace les courbes

    ### PM2_5

    # albi sale PM 2_5
    traceur_albiSalePM2_5 = TraceurCourbeAvecSeuil([albiSalePM2_5], "PM2_5")
    traceur_albiSalePM2_5.setTitreGraph(
        "Evolution de la concentration des PM2_5 dans le vestiaire sale du 27-02 au 13-03")
    traceur_albiSalePM2_5.set_lieu("le vestiaire sale")
    traceur_albiSalePM2_5.set_liste_seuil(seuils)
    traceur_albiSalePM2_5.set_liste_nom_seuil(["seuil 24h", "seuil année"])
    traceur_albiSalePM2_5.set_dir_path("albi/pm2_5/")
    traceur_albiSalePM2_5.set_fig_name("courbeAlbiSalePM2_5")
    traceur_albiSalePM2_5.draw_graph()

    # albi propre PM 2_5
    traceur_albiProprePM2_5 = TraceurCourbeAvecSeuil([albiProprePM2_5], "PM2_5")
    traceur_albiProprePM2_5.setTitreGraph(
        "Evolution de la concentration des PM2_5 dans le vestiaire propre du 27-02 au 13-03")
    traceur_albiProprePM2_5.set_lieu("le vestiaire propre")
    traceur_albiProprePM2_5.set_liste_seuil(seuils)
    traceur_albiProprePM2_5.set_liste_nom_seuil(["seuil 24h", "seuil année"])
    traceur_albiProprePM2_5.set_dir_path("albi/pm2_5/")
    traceur_albiProprePM2_5.set_fig_name("courbeAlbiProprePM2_5")
    traceur_albiProprePM2_5.draw_graph()

    # albi propre PM 2_5
    traceur_albiRemisePM2_5 = TraceurCourbeAvecSeuil([albiRemisePM2_5], "PM2_5")
    traceur_albiRemisePM2_5.setTitreGraph("Evolution de la concentration des PM2_5 dans la remise du 27-02 au 13-03")
    traceur_albiRemisePM2_5.set_lieu("la remise")
    traceur_albiRemisePM2_5.set_liste_seuil(seuils)
    traceur_albiRemisePM2_5.set_liste_nom_seuil(["seuil 24h", "seuil année"])
    traceur_albiRemisePM2_5.set_dir_path("albi/pm2_5/")
    traceur_albiRemisePM2_5.set_fig_name("courbeAlbiRemisePM2_5")
    traceur_albiRemisePM2_5.draw_graph()
