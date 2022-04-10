from analyses_mesures.courbes_avec_seuils_generator.TraceurCourbeAvecSeuil import TraceurCourbeAvecSeuil

albiSalePM10 = "../mesures/albi_mesures/albiSalePM10.csv"
albiProprePM10 = "../mesures/albi_mesures/albiProprePM10.csv"
albiRemisePM10 = "../mesures/albi_mesures/albiRemisePM10.csv"

op_albi = "../mesures/op_albi.xlsx"

seuils = [45, 15]  # 24h, année
nom_seuils = ["seuil 24h", "seuil année"]


def traceur_pm10_albi():
    # On trace les courbes

    ### PM10

    # albi sale PM 10
    traceur_albiSalePM10 = TraceurCourbeAvecSeuil([albiSalePM10], "PM10")
    traceur_albiSalePM10.setTitreGraph(
        "Evolution de la concentration des PM10 dans le vestiaire sale d'albi'")
    traceur_albiSalePM10.set_lieu("le vestiaire sale")
    traceur_albiSalePM10.set_op_albi(op_albi)
    traceur_albiSalePM10.set_liste_seuil(seuils)
    traceur_albiSalePM10.set_liste_nom_seuil(nom_seuils)
    traceur_albiSalePM10.set_dir_path("albi/pm10/")
    traceur_albiSalePM10.set_fig_name("courbeAlbiSalePM10")
    traceur_albiSalePM10.draw_graph()

    # albi propre PM 10
    traceur_albiProprePM10 = TraceurCourbeAvecSeuil([albiProprePM10], "PM10")
    traceur_albiProprePM10.set_op_albi(op_albi)
    traceur_albiProprePM10.setTitreGraph(
        "Evolution de la concentration des PM10 dans le vestiaire propre d'albi'")
    traceur_albiProprePM10.set_lieu("le vestiaire propre")
    traceur_albiProprePM10.set_liste_seuil(seuils)
    traceur_albiProprePM10.set_liste_nom_seuil(nom_seuils)
    traceur_albiProprePM10.set_dir_path("albi/pm10/")
    traceur_albiProprePM10.set_fig_name("courbeAlbiProprePM10")
    traceur_albiProprePM10.draw_graph()

    # albi propre PM 10
    traceur_albiRemisePM10 = TraceurCourbeAvecSeuil([albiRemisePM10], "PM10")
    # traceur_albiRemisePM10.set_op_albi(op_albi)
    traceur_albiRemisePM10.setTitreGraph("Evolution de la concentration des PM10 dans la remise d'albi")
    traceur_albiRemisePM10.set_lieu("la remise")
    traceur_albiRemisePM10.set_liste_seuil(seuils)
    traceur_albiRemisePM10.set_liste_nom_seuil(nom_seuils)
    traceur_albiRemisePM10.set_dir_path("albi/pm10/")
    traceur_albiRemisePM10.set_fig_name("courbeAlbiRemisePM10")
    traceur_albiRemisePM10.draw_graph()
