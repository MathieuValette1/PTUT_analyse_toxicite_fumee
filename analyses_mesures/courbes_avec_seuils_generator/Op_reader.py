from datetime import datetime

import pandas as pd


class Op_reader:

    def __init__(self):
        self.df_operations = ""

    @staticmethod
    def dateparse(dates):
        return datetime.strptime(dates, '%Y-%m-%d %H:%M:%S')


