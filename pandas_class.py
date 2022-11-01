import pandas as pd 

data_set = {
    'name': ['john','jane','joe','jack','jill'],
    'marks': [90,80,70,60,50]
}

df = pd.DataFrame(data_set)

print(df)

###

arr = [i for i in range(10)]

ps = pd.Series(arr)

print(ps)

###

ps = pd.Series(arr, index=['a','b','c','d','e','f','g','h','i','j'])

# print(ps)

print(ps['a'])

calories = {
    "day1": 420,
    "day2": 380,
    "day3": 390,
    "day4": 420,
}

p_calories = pd.Series(calories)
print(p_calories)

df = DataFrame(calories, index=['day1','day2','day3','day4'])
print(df.loc['day2'])