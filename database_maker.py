import pandas as pd
import random

# choose the number of points you want in the data set by changing the number below
Size = 1000
names = list(pd.read_csv("./baby-names.csv")["name"][:Size])
cities = list(pd.read_csv("./worldcities.csv")["city"][:Size])

INCOME_UPPER = 1_000_000
INCOME_LOWER = 1000
incomes = []
for i in range(1000):
    incomes.append(random.randint(INCOME_LOWER,INCOME_UPPER))


# Age
AGE_LOWER = 15
AGE_UPPER = 101
ages = []
for i in range(1000):
    ages.append(random.randint(AGE_LOWER,AGE_UPPER))

# Receiving the pension already?
# TODO: Eliminate possibilty of true for a person below 60 or earning a lot
receiving = [True, False]
recips = []
for i in range(1000):
    recips.append(random.choice(receiving))

data = {
    'name': names,
    'age': ages,
    "income": incomes,
    "receiving pension": recips,
    "cities": cities,
    }

final_dataset = pd.DataFrame(data)
final_dataset.to_csv("./citizens_database.csv")
print(final_dataset)
