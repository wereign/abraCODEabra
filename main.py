import pandas as pd

from database_maker import Dataset

AGE_OLD = 60   # Current cut off age for NSAP
INCOME_BPL = 11000   # Made up BPL criteria

dataset_form = Dataset(size_dataset=1_00_000_000,
                  income_lower=1000, income_upper=20000,
                  age_lower=15, age_higher=100)

nsap_dataset = dataset_form.make_nsap_database(5_000_000)  # making a NSAP database
dataset = dataset_form.make_database(nsap_dataset)     # Making a general citizens database

# Current age filter > 60, income less than 11,000.
# Simultaneously filtering out the eligible citizens
filtered_dataset = dataset[(dataset.age >= AGE_OLD) &
                           (dataset.income <= INCOME_BPL)]

# Checking for the people in the filtered dataset who are already receiving the pension
final_dataset = filtered_dataset.merge(nsap_dataset.drop_duplicates(), on=["name", "age", "income", "area"], how="left", indicator="Origin")
final_dataset = final_dataset[final_dataset.Origin == "left_only"]


# Grouping the data area wise
grouped_dataset = final_dataset.groupby("area")

# Finding all the cities in the filtered_dataset
all_areas = final_dataset.area.unique()
area_wise = []

for area_ in all_areas:
    temp = grouped_dataset.get_group(area_)
    area_wise.append(temp)

for area in area_wise:
    print("____________NEW CITY_____________")
    print()
    print()
    print(area)

