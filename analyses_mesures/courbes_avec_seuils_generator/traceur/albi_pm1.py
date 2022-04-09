from analyses_mesures.courbes_avec_seuils_generator.TraceurCourbeAvecSeuil import TraceurCourbeAvecSeuil

albiSalePM1 = "../mesures/albi_mesures/albiSalePM1.csv"
albiProprePM1 = "../mesures/albi_mesures/albiProprePM1.csv"
albiRemisePM1 = "../mesures/albi_mesures/albiRemisePM1.csv"

seuils = []


def traceur_pm1_albi():
    # On trace les courbes

    ### PM1

    # albi sale PM 1
    traceur_albiSalePM1 = TraceurCourbeAvecSeuil([albiSalePM1], "PM1")
    traceur_albiSalePM1.setTitreGraph(
        "Evolution de la concentration des PM1 dans le vestiaire sale d'albi'")
    traceur_albiSalePM1.set_lieu("le vestiaire sale")
    traceur_albiSalePM1.set_liste_seuil(seuils)
    traceur_albiSalePM1.set_liste_nom_seuil([])
    traceur_albiSalePM1.set_dir_path("albi/pm1/")
    traceur_albiSalePM1.set_fig_name("courbeAlbiSalePM1")
    traceur_albiSalePM1.draw_graph()

    # albi propre PM 1
    traceur_albiProprePM1 = TraceurCourbeAvecSeuil([albiProprePM1], "PM1")
    traceur_albiProprePM1.setTitreGraph(
        "Evolution de la concentration des PM1 dans le vestiaire propre d'albi'")
    traceur_albiProprePM1.set_lieu("le vestiaire sale")
    traceur_albiProprePM1.set_liste_seuil(seuils)
    traceur_albiProprePM1.set_liste_nom_seuil([])
    traceur_albiProprePM1.set_dir_path("albi/pm1/")
    traceur_albiProprePM1.set_fig_name("courbeAlbiProprePM1")
    traceur_albiProprePM1.draw_graph()

    # albi propre PM 1
    traceur_albiRemisePM1 = TraceurCourbeAvecSeuil([albiRemisePM1], "PM1")
    traceur_albiRemisePM1.setTitreGraph("Evolution de la concentration des PM1 dans la remise d'albi'")
    traceur_albiRemisePM1.set_lieu("la remise")
    traceur_albiRemisePM1.set_liste_seuil(seuils)
    traceur_albiRemisePM1.set_liste_nom_seuil([])
    traceur_albiRemisePM1.set_dir_path("albi/pm1/")
    traceur_albiRemisePM1.set_fig_name("courbeAlbiRemisePM1")
    traceur_albiRemisePM1.draw_graph()
