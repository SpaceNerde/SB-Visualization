import pandas as pd
import requests
import json
import csv
import re

import tkinter as tk

from widgets.ssd_cneos import SSD_CNEOS
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

class App():
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('1600x800')
        self.root.rowconfigure(0, weight = 1)
        self.root.columnconfigure(0, weight = 1)

    
    def load_widgets(self):
        SSD_CNEOS(self.root, df)

    def run(self):
        self.root.mainloop()

if __name__ == '__main__':
    app = App()
    app.load_widgets()
    app.run()