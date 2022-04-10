# Path des csv à analyser
from analyses_mesures.courbes_avec_seuils_generator.Op_reader import Op_reader
from analyses_mesures.courbes_avec_seuils_generator.traceur.albi_co2 import traceur_CO2_albi
from analyses_mesures.courbes_avec_seuils_generator.traceur.albi_cov import traceur_COV_albi
from analyses_mesures.courbes_avec_seuils_generator.traceur.albi_pm1 import traceur_pm1_albi
from analyses_mesures.courbes_avec_seuils_generator.traceur.albi_pm10 import traceur_pm10_albi
from analyses_mesures.courbes_avec_seuils_generator.traceur.albi_pm2_5 import traceur_pm2_5_albi
from analyses_mesures.courbes_avec_seuils_generator.traceur.mazamet_2_5 import traceur_pm2_5_mazamet
from analyses_mesures.courbes_avec_seuils_generator.traceur.mazamet_cov import traceur_COV_mazamet
from analyses_mesures.courbes_avec_seuils_generator.traceur.mazamet_pm1 import traceur_pm1_mazamet
from analyses_mesures.courbes_avec_seuils_generator.traceur.mazamet_pm10 import traceur_pm10_mazamet
from analyses_mesures.courbes_avec_seuils_generator.traceur.mazmet_co2 import traceur_CO2_mazamet

if __name__ == '__main__':

    print("Traçage des courbes...")
    print("Pm10..")
    traceur_pm10_mazamet()
    traceur_pm10_albi()

    print("PM2,5...")
    traceur_pm2_5_mazamet()
    traceur_pm2_5_albi()

    print("PM1...")
    traceur_pm1_mazamet()
    traceur_pm1_albi()

    print("COV...")
    traceur_COV_mazamet()
    traceur_COV_albi()

    print("CO2...")
    traceur_CO2_mazamet()
    traceur_CO2_albi()

    print('Toutes les courbes sont tracées')
