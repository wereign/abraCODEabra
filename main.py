import pandas as pd

from database_maker import Dataset

dataset = Dataset(size_dataset=10000,
                  income_lower=1000, income_upper=20000,
                  age_lower=15, age_higher=100).make_database()

AGE_OLD = 60
INCOME_BPL = 11000


def filtering(series_person):
    return (series_person[1] >= AGE_OLD  # checking if the person is above old age
            and series_person[2] < INCOME_BPL  # checking if the person is bpl
            and not (series_person[3]))  # checking if person is receiving the pension or not


# Current age filter > 60, income less than 11,000.
filtered_dataset = dataset[(dataset.age >= AGE_OLD) &
                           (dataset.income <= INCOME_BPL) &
                           (dataset.receiving_pension == False)]


# print("THIS IS THE FILTERED DATASET")
# print(filtered_dataset)


# now categorizing the filtered_dataset by the areas



grouped_dataset = filtered_dataset.groupby("area")
all_cities = filtered_dataset.area.unique()
# print(all_cities)

for city in all_cities:
    print("____________NEW CITY_____________")
    print()
    print()
    print(grouped_dataset.get_group(city))
