from database_maker import Dataset

AGE_OLD = 60   # Current cut off age for NSAP
INCOME_BPL = 11000   # Made up BPL criteria


dataset = Dataset(size_dataset=10000,
                  income_lower=1000, income_upper=20000,
                  age_lower=15, age_higher=100).make_database()

# Current age filter > 60, income less than 11,000.
filtered_dataset = dataset[(dataset.age >= AGE_OLD) &
                           (dataset.income <= INCOME_BPL) &
                           (dataset.receiving_pension == "Not Receiving")]

# Grouping the data area wise
grouped_dataset = filtered_dataset.groupby("area")

# Finding all the cities in the filtered_dataset
all_areas = filtered_dataset.area.unique()
area_wise = []

for area_ in all_areas:
    temp = grouped_dataset.get_group(area_)
    area_wise.append(temp)

for area in area_wise:
    print("____________NEW CITY_____________")
    print()
    print()
    print(area)

