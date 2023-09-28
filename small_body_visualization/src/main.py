import pandas as pd
import requests
import json
import csv
import re

import sys
from PyQt5.QtWidgets import QApplication, QTableView
from PyQt5.QtCore import QAbstractTableModel, Qt


# uncomment to get Data

'''
req = requests.get("https://ssd-api.jpl.nasa.gov/cad.api", params={
    'diameter': False,
    'fullname': True,
    'nea-comet': False,
    'comet': False,
    'nea': False,
    'pha': False,
    'neo': False,
    }
)
fields = req.json()['fields']
data = req.json()['data']

print(json.dumps(data, indent=4))
print(json.dumps(fields, indent=4))

df = pd.DataFrame(columns=fields[::-1], data=[d[::-1] for d in data])

df.to_csv('data.csv', index=False)
'''

df = pd.read_csv('data.csv')

class App(QAbstractTableModel):
    def __init__(self, data):
        QAbstractTableModel.__init__(self)
        self._data = data

    def rowCount(self, parent=None):
        return self._data.shape[0]

    def columnCount(self, parnet=None):
        return self._data.shape[1]

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole:
                return str(self._data.iloc[index.row(), index.column()])
        return None

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self._data.columns[col]
        return None

if __name__ == '__main__':
    app = QApplication(sys.argv)
    model = App(df)
    view = QTableView()
    view.setModel(model)
    view.resize(800, 600)
    view.show()
    sys.exit(app.exec_())