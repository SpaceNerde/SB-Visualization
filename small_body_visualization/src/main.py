import pandas as pd
import requests
import json
import csv
import re

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

print(df)