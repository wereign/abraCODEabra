import pandas as pd

from database_maker import Dataset

AGE_OLD = 60   # Current cut off age for NSAP
INCOME_BPL = 11000   # Made up BPL criteria

dataset_form = Dataset(size_dataset=2_000_000,
                  income_lower=1000, income_upper=20000,
                  age_lower=15, age_higher=100)

nsap_dataset = dataset_form.make_nsap_database(50000)
dataset = dataset_form.make_database(nsap_dataset)

# Current age filter > 60, income less than 11,000.
filtered_dataset = dataset[(dataset.age >= AGE_OLD) &
                           (dataset.income <= INCOME_BPL)]

final_dataset = filtered_dataset.merge(nsap_dataset.drop_duplicates(), on=["name", "age", "income", "area"], how="left", indicator="Origin")
final_dataset = final_dataset[final_dataset.Origin == "left_only"]


# print(filtered_dataset)
# print()
# print('___________________')
# print(final_dataset)



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

