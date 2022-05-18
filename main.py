import pandas as pd

from database_maker import Dataset

AGE_OLD = 60   # Current cut off age for NSAP
INCOME_BPL = 11000   # Made up BPL criteria


datasets = Dataset(size_dataset=1000,
                  income_lower=1000, income_upper=20000,
                  age_lower=15, age_higher=100).make_database()

nsap_dataset = datasets[0].to_dict()
dataset = datasets[1]

# Current age filter > 60, income less than 11,000.
filtered_dataset = dataset[(dataset.age >= AGE_OLD) &
                           (dataset.income <= INCOME_BPL)]

# Grouping the data area wise
grouped_dataset = filtered_dataset.groupby("area")

# Finding all the cities in the filtered_dataset
all_areas = filtered_dataset.area.unique()
area_wise = []

for area_ in all_areas:
    temp = grouped_dataset.get_group(area_)
    area_wise.append(temp)

# for area in area_wise:
#     print("____________NEW CITY_____________")
#     print()
#     print()
#     print(area)

one_place = area_wise[0]
place_dict = one_place.to_dict()
# print(place_dict)

final_names = []
final_ages = []
final_income = []
final_area = []

for key in place_dict['name']:
    if not ((place_dict['name'][key] in nsap_dataset['name']) and (place_dict['age'][key] in nsap_dataset['age']) and
            (place_dict['income'][key] in nsap_dataset['income']),
            (place_dict['area'][key] in nsap_dataset['area'])):

        final_names.append(place_dict['name'][key])
        final_ages.append(place_dict['age'][key])
        final_income.append(place_dict['income'][key])

        area_temp = pd.DataFrame(data={"NAME":final_names, "AGE":final_ages})
        print("Here")
        print(area_temp)

    else:
        pass



# making an NSAP dataset.


