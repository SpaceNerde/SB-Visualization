import pandas as pd
import requests
import json
import csv
import re

req = requests.get("https://ssd-api.jpl.nasa.gov/sb_sat.api", params={
    'orb': 1,
    'sigma': 1,
    'phys-par': 1,
    'fullname': 1,
    'class': 1
    }
)

data = req.json()['data']

df = pd.DataFrame([item["sat"] for item in data])

df['prov_num'] = pd.to_numeric(df['prov_num'], errors='coerce')

df.sort_values(by='prov_num', inplace=True)

df[['number', 'name']] = df['sat_fullname'].str.extract(r'\((\d+)\) (.*)')

df.drop(columns='sat_fullname', inplace=True)

df.to_csv('data.csv', index=False)

print(df)
