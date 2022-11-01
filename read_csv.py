import pandas as pd 
import numpy as numpy
import requests
import json

# pd = pd.read_csv('')

def download_csv(url):
    r = requests.get(url)
    with open('data.csv', 'wb') as f:
        f.write(r.content)

import os

if not os.path.exists('data.csv'):
    download_csv('https://www.sample-videos.com/csv/Sample-Spreadsheet-10-rows.csv')


df = pd.read_csv('data.csv')
print(df)

todos = requests.get("https://jsonplaceholder.typicode.com/todos").json()
df = pd.DataFrame(todos)

print(df.head())


