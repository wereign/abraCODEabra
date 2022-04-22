from generating_dataset import data, Citizen

citizens_list = data


# First filter is area wise
class Area:
    def __init__(self, area_name):
        self.area_name = area_name
        self.citizens = []

    def __repr__(self):
        return f"""AREA: {self.area_name.upper()}\n{self.citizens}"""

    def __str__(self):
        return self.__repr__()

    def insert_citizen(self, person: Citizen):
        if type(person) == list:
            self.citizens.extend(person)
        if isinstance(person, Citizen):
            self.citizens.append(person)


# Putting all the data into area wise sorted lists.
places = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

area_dict = {}

for pers in citizens_list:

    if pers.area in area_dict:
        area_dict[pers.area].append(pers)

    else:
        area_dict[pers.area] = []
        area_dict[pers.area].append(pers)

places = []
for place in area_dict:
    temp_place = Area(place)
    temp_place.insert_citizen(area_dict[place])
    places.append(temp_place)

def criteria_1(x):
    return x.age


for place in places:
    place.citizens = sorted(place.citizens,key=criteria_1)
    print(place.citizens)
    place.citizens = list(filter(lambda x: x.age > 35, place.citizens))
    print(place.citizens)
    place.citizens = list(filter(lambda x: x.income < 4500, place.citizens))
    print(place.citizens)
    place.citizens = list(filter(lambda x: not(x.receiving_bpl), place.citizens))
    print(place.citizens)




