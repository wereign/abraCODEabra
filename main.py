from database_maker import Dataset

dataset = Dataset(size_dataset=2000,
                  income_lower=1000, income_upper=20000,
                  age_lower=15, age_higher=100).make_database()

# print(dataset.__doc__)

# Current age filter > 60, income less than 11,000.
print(dataset)
filtered_dataset = dataset[(dataset.age >= 60) & (dataset.income <= 11000) & (dataset.receiving_pension == False)]
# isha the above line is there for filtering, i have done all the filtering in one go,you will need to do the conditions one by one

print(filtered_dataset)
