import pandas as pd
import numpy as np
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

        self.NSAP_Names = []
        self.NSAP_Area = []
        self.NSAP_Incomes = []
        self.NSAP_Ages = []

    def make_nsap_database(self):

        for step in range(2000):
            self.NSAP_Names.append(random.choice(self.names_list))
            self.NSAP_Area.append(random.choice(self.areas_list))
            self.NSAP_Incomes.append(random.randint(2000, 11000))
            self.NSAP_Ages.append(random.randint(60, 101))

        nsap = {
            ""
            'name': self.NSAP_Names,
            'age': self.NSAP_Ages,
            "income": self.NSAP_Incomes,
            "area": self.NSAP_Area,
        }

        nsap_dataframe = pd.DataFrame(nsap)
        return nsap_dataframe


    def make_database(self):
        for step in range(self.size):
            self.names.append(random.choice(self.names_list))
            self.areas.append(random.choice(self.areas_list))
            self.incomes.append(random.randint(self.income_lower, self.income_upper))
            # self.recips.append(random.choice(self.receiving))
            self.ages.append(random.randint(self.age_lower, self.age_upper))

        data = {
            ""
            'name': self.names,
            'age': self.ages,
            "income": self.incomes,
            # "receiving_pension": self.recips,
            "area": self.areas,
        }
        temp_data = pd.DataFrame(data)
        temp_nsap = self.make_nsap_database()
        final_dataset = temp_data.append(temp_nsap)
        # final_dataset.to_csv("./citizens_database.csv"

        # dataset["receiving_pension"] = np.where(dataset.age >= 60,)
        return temp_nsap,final_dataset


# dataset = Dataset(size_dataset=100, income_lower=100, income_upper=1000, age_lower=15, age_higher=69)
# data = dataset.make_database()
# print(data)

# inserting all the nsap database names into the main database, adding more eligible persons.
# use the nsap databse to assign a true value for the values in the main database.
