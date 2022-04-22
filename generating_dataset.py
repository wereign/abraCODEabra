import random


# This is a class.
class Citizen:
    def __init__(self, name, age, income, area, receiving_bpl):
        self.name = name
        self.age = age
        self.income = income
        self.area = area
        self.receiving_bpl = receiving_bpl

    def __str__(self):
        return f""" Name:{self.name} Age:{self.age} Income:{self.income} Area:{self.area} Receiving BPL:{self.receiving_bpl}\n"""

    def __repr__(self):
        return self.__str__()

    @staticmethod
    def make_database(size):
        dataset = []
        for i in range(50):
            temp_name = random.choice(names)
            temp_area = random.choice(places)
            temp_income = random.randint(4000, 5000)
            temp_age = random.randint(25, 60)
            temp_bpl = random.choice([True,False])

            temp_person = Citizen(temp_name, temp_age, temp_income, temp_area,temp_bpl)
            dataset.append(temp_person)

        return dataset




# Making a list to store the instances ,i.e each person
data = []

eg_person = Citizen("Arun", 69, 69420420, "Bhosri",False)

places = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
names = ['h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']

# Let's say we want to make 50 instances

data = Citizen.make_database(50)
# print(data)
