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

grouped_dataset = filtered_dataset.groupby("area")
all_cities = filtered_dataset.area.unique()

areawise = []

for city in all_cities:
    temp = grouped_dataset.get_group(city)
    areawise.append(temp)

for area in areawise:
    print("____________NEW CITY_____________")
    print()
    print()
    print(area)

