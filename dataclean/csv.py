import pandas as pd


class Csv(object):
    def __init__(self, path):
        self.path = path;

    def read_csv(self):
        return pd.read_csv(self.path)
