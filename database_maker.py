import pandas as pd
import random


# making a class

class Dataset:
    def __init__(self, size_dataset, income_lower, income_upper, age_lower, age_higher, names_file="./baby-names.csv",
                 area_file="./worldcities.csv"):
        self.income_lower = income_lower
        self.income_upper = income_upper
        self.age_lower = age_lower
        self.age_upper = age_higher
        self.size = size_dataset

        self.receiving = ["Receiving", "Not Receiving"]

        self.names = []
        self.areas = []
        self.incomes = []
        self.recips = []
        self.ages = []
        self.names_list = list(pd.read_csv(names_file)["name"])
        self.areas_list = list(pd.read_csv(area_file)["city"][800:1000])

    def make_database(self):
        for step in range(self.size):
            self.names.append(random.choice(self.names_list))
            self.areas.append(random.choice(self.areas_list))
            self.incomes.append(random.randint(self.income_lower, self.income_upper))
            self.recips.append(random.choice(self.receiving))
            self.ages.append(random.randint(self.age_lower, self.age_upper))

        data = {
            ""
            'name': self.names,
            'age': self.ages,
            "income": self.incomes,
            "receiving_pension": self.recips,
            "area": self.areas,
        }

        final_dataset = pd.DataFrame(data)
        # final_dataset.to_csv("./citizens_database.csv")
        return final_dataset

# dataset = Dataset(size_dataset=100,income_lower=100,income_upper=1000,age_lower=15,age_higher=69)
# new = dataset.make_database()
# print(new)