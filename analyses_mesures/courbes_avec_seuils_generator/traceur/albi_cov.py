from analyses_mesures.courbes_avec_seuils_generator.TraceurCourbeAvecSeuil import TraceurCourbeAvecSeuil

albiSaleCOV = "../mesures/albi_mesures/albiSaleCOV.csv"
albiPropreCOV = "../mesures/albi_mesures/albiPropreCOV.csv"
albiRemiseCOV = "../mesures/albi_mesures/albiRemiseCOV.csv"

op_albi = "../mesures/op_albi.xlsx"

seuils = [250, 500, 1000, 3000]
nom_seuils = ["Niveau 1", "Niveau 2", "Niveau 3", "Niveau 4", "Niveau 5"]

def traceur_COV_albi():
    # On trace les courbes

    ### COV

    # albi sale PM 10
    traceur_albiSaleCOV = TraceurCourbeAvecSeuil([albiSaleCOV], "COV")
    traceur_albiSaleCOV.setTitreGraph(
        "Evolution de la concentration des COV dans le vestiaire sale d'albi")
    traceur_albiSaleCOV.set_lieu("le vestiaire sale")
    traceur_albiSaleCOV.set_liste_seuil(seuils)
    traceur_albiSaleCOV.set_op_albi(op_albi)
    traceur_albiSaleCOV.set_liste_nom_seuil(nom_seuils)
    traceur_albiSaleCOV.set_dir_path("albi/COVt/")
    traceur_albiSaleCOV.set_fig_name("courbeAlbiSaleCOV")
    traceur_albiSaleCOV.draw_graph()

    # albi propre COV
    traceur_albiPropreCOV = TraceurCourbeAvecSeuil([albiPropreCOV], "COV")
    traceur_albiPropreCOV.setTitreGraph(
        "Evolution de la concentration des COV dans le vestiaire propre d'albi")
    traceur_albiPropreCOV.set_lieu("le vestiaire propre")
    traceur_albiPropreCOV.set_op_albi(op_albi)
    traceur_albiPropreCOV.set_liste_seuil(seuils)
    traceur_albiPropreCOV.set_liste_nom_seuil(nom_seuils)
    traceur_albiPropreCOV.set_dir_path("albi/COVt/")
    traceur_albiPropreCOV.set_fig_name("courbeAlbiPropreCOV")
    traceur_albiPropreCOV.draw_graph()

    # albi propre COV
    traceur_albiRemiseCOV = TraceurCourbeAvecSeuil([albiRemiseCOV], "COV")
    traceur_albiRemiseCOV.setTitreGraph("Evolution de la concentration des COV dans la remise d'albi")
    traceur_albiRemiseCOV.set_lieu("la remise")
    traceur_albiRemiseCOV.set_op_albi(op_albi)
    traceur_albiRemiseCOV.set_liste_seuil(seuils)
    traceur_albiRemiseCOV.set_liste_nom_seuil(nom_seuils)
    traceur_albiRemiseCOV.set_dir_path("albi/COVt/")
    traceur_albiRemiseCOV.set_fig_name("courbeAlbiRemiseCOV")
    traceur_albiRemiseCOV.draw_graph()
