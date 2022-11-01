import pandas as pd
import requests
import numpy as np


# df = pd.DataFrame(np.random.randn(5, 3), columns=['col1', 'col2', 'col3'])
# df.apply(lambda x: x.max() - x.min())
# print(df)

618091 -0.827185
1  1.247302  0.606679 -0.779310
2 -1.156322 -0.424120 -1.919348
3  0.140348  0.926153 -0.413919
4  0.835529  1.037652 -0.420970



df = pd.read_csv('machine_readable_business_employment_data_june_2022_quarter.csv')
print(df)
[20254 rows x 14 columns]



df.na_count()



df = pd. DataFrame(np. random. randint(0,10,size=(10, 3)), columns=list('ABC'))
print(df)
newdf = df.replace(5, 10)
print(newdf)



data = requests.get("https://jsonplaceholder.typicode.com/albums").json()
df = pd.DataFrame(data)
print(df.head())



