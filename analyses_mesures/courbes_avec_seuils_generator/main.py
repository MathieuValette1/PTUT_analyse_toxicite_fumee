# Path des csv à analyser
from analyses_mesures.courbes_avec_seuils_generator.traceur.mazamet_2_5 import traceur_pm2_5
from analyses_mesures.courbes_avec_seuils_generator.traceur.mazamet_cov import traceur_COV
from analyses_mesures.courbes_avec_seuils_generator.traceur.mazamet_pm1 import traceur_pm1
from analyses_mesures.courbes_avec_seuils_generator.traceur.mazamet_pm10 import traceur_pm10

if __name__ == '__main__':
    print("Traçage des courbes...")
    traceur_pm10()
    traceur_pm2_5()
    traceur_pm1()
    traceur_COV()
    print('Toutes les courbes sont tracées')
