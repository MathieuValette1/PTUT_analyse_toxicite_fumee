from analyses_mesures.courbes_avec_seuils_generator.TraceurCourbeAvecSeuil import TraceurCourbeAvecSeuil

albiSaleCO2 = "../mesures/albi_mesures/albiSaleCO2.csv"
albiPropreCO2 = "../mesures/albi_mesures/albiPropreCO2.csv"
albiRemiseCO2 = "../mesures/albi_mesures/albiRemiseCO2.csv"

op_albi = "../mesures/op_albi.xlsx"

seuils = []  # 24h, année
nom_seuils = []


def traceur_CO2_albi():
    # On trace les courbes

    ### CO2

    # albi sale PM 10
    traceur_albiSaleCO2 = TraceurCourbeAvecSeuil([albiSaleCO2], "CO2")
    traceur_albiSaleCO2.setTitreGraph(
        "Evolution de la concentration des CO2 dans le vestiaire sale d'albi'")
    traceur_albiSaleCO2.set_lieu("le vestiaire sale")
    traceur_albiSaleCO2.set_liste_seuil(seuils)
    traceur_albiSaleCO2.set_liste_nom_seuil(nom_seuils)
    traceur_albiSaleCO2.set_op_albi(op_albi)
    traceur_albiSaleCO2.set_ylabel('ppm')
    traceur_albiSaleCO2.set_dir_path("albi/CO2/")
    traceur_albiSaleCO2.set_fig_name("courbeAlbiSaleCO2")
    traceur_albiSaleCO2.draw_graph()

    # albi propre PM 10
    traceur_albiPropreCO2 = TraceurCourbeAvecSeuil([albiPropreCO2], "CO2")
    traceur_albiPropreCO2.setTitreGraph(
        "Evolution de la concentration des CO2 dans le vestiaire propre d'albi'")
    traceur_albiPropreCO2.set_lieu("le vestiaire propre")
    traceur_albiPropreCO2.set_liste_seuil(seuils)
    traceur_albiPropreCO2.set_op_albi(op_albi)
    traceur_albiPropreCO2.set_ylabel('ppm')
    traceur_albiPropreCO2.set_liste_nom_seuil(nom_seuils)
    traceur_albiPropreCO2.set_dir_path("albi/CO2/")
    traceur_albiPropreCO2.set_fig_name("courbeAlbiPropreCO2")
    traceur_albiPropreCO2.draw_graph()

    # albi remise PM 10
    traceur_albiRemiseCO2 = TraceurCourbeAvecSeuil([albiRemiseCO2], "CO2")
    traceur_albiRemiseCO2.setTitreGraph("Evolution de la concentration des CO2 dans la remise d'albi'")
    traceur_albiRemiseCO2.set_lieu("la remise")
    traceur_albiRemiseCO2.set_liste_seuil(seuils)
    traceur_albiRemiseCO2.set_op_albi(op_albi)
    traceur_albiRemiseCO2.set_liste_nom_seuil(nom_seuils)
    traceur_albiRemiseCO2.set_ylabel('ppm')
    traceur_albiRemiseCO2.set_dir_path("albi/CO2/")
    traceur_albiRemiseCO2.set_fig_name("courbeAlbiRemiseCO2")
    traceur_albiRemiseCO2.draw_graph()
