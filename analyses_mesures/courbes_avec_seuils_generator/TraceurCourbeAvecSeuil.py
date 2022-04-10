import seaborn as sns
import pandas as pd
from pylab import *
from datetime import datetime, timedelta

from .Op_reader import Op_reader

STORAGE_PATH = '../graphs/courbes_avec_seuils/'


class TraceurCourbeAvecSeuil:

    def __init__(self, listeDataframePath, typeMesure="", titre_graph="", lieu=""):
        self.typeMesure = typeMesure
        self.listeDataFramePath = listeDataframePath
        self.liste_deuxieme_dataframe_path = list()
        self.titre_graph = titre_graph
        self.listeDataFrame = list()
        self.liste_deuxieme_dataframe = list()
        self.lieu = lieu
        self.liste_lieu = list()
        self.xlabel = "Temps"
        self.ylabel = "ug/m^3"
        self.liste_seuil = list()
        self.liste_nom_seuil = list()
        self.deuxieme_ylabel = ""
        self.deuxieme_type_mesure = ""
        self.figname = ""
        self.dirpath = ""
        self.op_mazamet = ""  # path pour les données opérationnelles de mazamet
        self.op_albi = ""

    def add_dataframe(self, dataframe):
        self.listeDataFrame.append(dataframe)

    def set_liste_deuxieme_dataframe_path(self, liste_deuxieme_dataframe_path):
        self.liste_deuxieme_dataframe_path = liste_deuxieme_dataframe_path
        print(self.liste_deuxieme_dataframe_path)

    def add_second_dataframe(self, dataframe):
        self.liste_deuxieme_dataframe.append(dataframe)

    def add_liste_nom_seuil(self, nom_seuil):
        self.liste_nom_seuil.append(nom_seuil)

    def set_liste_nom_seuil(self, liste_nom_seuil):
        self.liste_nom_seuil = liste_nom_seuil

    def set_deuxieme_type_mesure(self, typemesure):
        self.deuxieme_type_mesure = typemesure

    def add_liste_seuil(self, liste_seuil):
        self.liste_seuil.append(liste_seuil)

    def set_liste_seuil(self, liste_seuil):
        self.liste_seuil = liste_seuil

    def setTitreGraph(self, graph_title):
        self.titre_graph = graph_title

    def setTypeMesure(self, typeMesure):
        self.typeMesure = typeMesure

    def set_lieu(self, lieu):
        self.lieu = lieu

    def set_fig_name(self, figname):
        self.figname = figname

    def set_dir_path(self, dirpath):
        self.dirpath = dirpath

    def set_xlabel(self, x_label):
        self.xlabel = x_label

    def set_ylabel(self, x_label):
        self.ylabel = x_label

    def set_deuxieme_ylabel(self, y_label):
        self.deuxieme_ylabel = y_label

    def set_liste_lieu(self, liste_lieu):
        self.liste_lieu = liste_lieu

    def set_op_mazamet(self, excel_path):
        self.op_mazamet = excel_path

    def set_op_albi(self, excel_path):
        self.op_albi = excel_path

    @staticmethod
    def _set_seuil_color():
        return ['green', 'yellow', 'orange', 'red', 'purple', 'pink', 'brown', 'blue', 'black']

    @staticmethod
    def dateparse(dates):
        return datetime.strptime(dates, '%Y-%m-%d %H:%M:%S')

    def csv_reader(self, csv_path):

        df = pd.read_csv(csv_path, sep=";", header=0,
                         names=['Date', self.typeMesure])
        df.iloc[:, 1:] = df.iloc[:, 1:].replace(',', '.', regex=True).astype(float)
        df["Date"] = pd.to_datetime(df["Date"])
        time_, value = self.transformToMean(df)
        df = pd.DataFrame({
            "Date": time_,
            "Value": value
        })

        df = df.set_index('Date')

        return df

    def fill_liste_deuxieme_DataFrame(self):
        for csv_path in self.liste_deuxieme_dataframe_path:
            print(csv_path)
            df = self.csv_reader(csv_path)
            self.liste_deuxieme_dataframe.append(df)

    def fill_listeDataFrame(self):
        for csv_path in self.listeDataFramePath:
            df = self.csv_reader(csv_path)
            self.listeDataFrame.append(df)

    @staticmethod
    def transformToMean(dataframe):
        dates = dataframe.iloc[:, 0]
        values = dataframe.iloc[:, 1]

        time_ = []
        value = []

        beginning = dates.loc[0]
        end = beginning + timedelta(hours=1)

        total = 0
        number_ = 0

        for i in range(dates.size):
            current = dates.loc[i]

            if beginning <= current <= end:
                number_ += 1
                total += values.loc[i]


            else:
                if number_ == 0:
                    time_.append(beginning)
                    value.append(values.loc[i])

                else:
                    time_.append(beginning)
                    value.append(total / number_)

                total = 0
                number_ = 0
                beginning = beginning + timedelta(hours=1)
                end = beginning + timedelta(hours=1)

        return time_, value

    def _set_label(self):
        if self.liste_deuxieme_dataframe:
            liste_label = list()
            if len(self.listeDataFrame) == 1:
                label = self.typeMesure + " dans " + self.lieu
                liste_label.append(label)
            else:
                if not self.liste_lieu:
                    for i in range(len(self.listeDataFrame)):
                        liste_label.append('[définir un lieu avec .set_liste_lieu()]')
                for lieu in self.liste_lieu:
                    liste_label.append(self.typeMesure + " dans " + lieu)
                if not self.liste_lieu:
                    for i in range(len(self.liste_deuxieme_dataframe)):
                        liste_label.append('[définir un lieu avec .set_liste_lieu()]')
                for lieu in self.liste_lieu:
                    liste_label.append(self.deuxieme_type_mesure + " dans " + lieu)
            return liste_label

        else:
            if len(self.listeDataFrame) == 1:
                label = self.typeMesure + " dans " + self.lieu
                return [label]
            else:
                liste_label = list()
                if not self.liste_lieu:
                    for i in range(len(self.listeDataFrame)):
                        liste_label.append('[définir un lieu avec .set_liste_lieu()]')
                for lieu in self.liste_lieu:
                    liste_label.append(self.typeMesure + " dans " + lieu)
                return liste_label

    def read_excel(self, excel_path):
        self.df_operations = pd.read_excel(excel_path, usecols=[5, 9, 10], names=['nature', "date_fin", "heure_fin"])
        self.df_operations['date_heure_fin'] = self.df_operations['date_fin'] + ' ' + self.df_operations['heure_fin']
        self.df_operations = self.df_operations.drop('date_fin', axis=1).drop('heure_fin', axis=1)
        self.df_operations["date_heure_fin"] = pd.to_datetime(self.df_operations["date_heure_fin"])

        return self.df_operations

    def draw_graph(self):

        self.fill_listeDataFrame()

        if self.liste_deuxieme_dataframe_path:
            self.fill_liste_deuxieme_DataFrame()

        largeur = 20
        hauteur = 10
        sns.set(rc={'figure.figsize': (largeur, hauteur)})  # largeur hauteur

        # plt.figure()

        fig, ax = plt.subplots()
        ax.set_title(self.titre_graph)
        liste_label = self._set_label()

        for i in range(len(self.listeDataFrame)):
            ax.plot(self.listeDataFrame[i], label=liste_label[i])

        for i in range(len(self.liste_seuil)):
            ax.axhline(self.liste_seuil[i], label=self.liste_nom_seuil[i], color=self._set_seuil_color()[i])

        if self.op_mazamet:
            df = self.read_excel(self.op_mazamet)
            dates = list(df['date_heure_fin'])
            natures = list(df['nature'])
            for i in range(len(dates)):
                ax.axvline(dates[i], color='red')
                text(dates[i], ax.get_ylim()[1] * 0.75, natures[i], rotation=90, horizontalalignment='right',
                     verticalalignment='center',
                     backgroundcolor='yellow',
                     fontsize='smaller'
                     )

        if self.op_albi:
            df = self.read_excel(self.op_albi)
            dates = list(df['date_heure_fin'])
            natures = list(df['nature'])
            for i in range(len(dates)):
                ax.axvline(dates[i], color='red')
                text(dates[i], ax.get_ylim()[1]*0.75,  natures[i], rotation=90,horizontalalignment='right',
                     verticalalignment='center',
                     backgroundcolor='yellow',
                    fontsize = 'smaller'
                    )

        if self.liste_deuxieme_dataframe:
            ax2 = ax.twinx()
            for i in range(len(self.liste_deuxieme_dataframe)):
                ax2.plot(self.liste_deuxieme_dataframe[i], label=self.deuxieme_ylabel)

        ax.set_xlabel(self.xlabel)
        ax.set_ylabel(self.ylabel)
        ax.legend()

        # plt.show()
        storage_path = STORAGE_PATH + self.dirpath
        plt.savefig(storage_path + self.figname)
        plt.close()
