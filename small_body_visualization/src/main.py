import pandas as pd
import requests

import tkinter as tk

from widgets.ssd_cneos import SSD_CNEOS
from widgets.legend import Legend

req = requests.get("https://ssd-api.jpl.nasa.gov/cad.api", params={
    'diameter': True,
    'fullname': True,
    }
)
fields = req.json()['fields']
data = req.json()['data']

df = pd.DataFrame(columns=fields[::-1], data=[d[::-1] for d in data])

df.to_csv('data.csv', index=False)

df = pd.read_csv('data.csv')

class App():
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('1800x500')
        self.root.rowconfigure(0, weight = 1)
        self.root.columnconfigure(0, weight = 1)
        self.root.title("Space's Small Body Visualization")
    
    def load_widgets(self):
        SSD_CNEOS(self.root, df).grid(row=0, sticky="nw" ,column=0, padx=23, pady=23)
        Legend(self.root).grid(row=1, column=0, sticky="nw", padx=23, pady=23)

    def run(self):
        self.root.mainloop()

if __name__ == '__main__':
    app = App()
    app.load_widgets()
    app.run()