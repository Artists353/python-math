class Building:
    year = None
    city = None
    people_in_house = None
    repair = None

    def __init__(self, year, city, repair, people_in_house):
        self.year = year
        self.city = city
        self.people_in_house = people_in_house
        self.repair = repair

class House(Building):
    def __init__(self, year, city, people_in_house, repair):
        super(House, self).__init__(year, city, people_in_house, repair)
        self.year = year
        self.city = city
        self.people_in_house = people_in_house
        self.repair = repair

    def get_info(self):
        with open("text.txt", "r", encoding="utf-8") as inf_build:
            inf_build_read = inf_build.read() 
            if inf_build_read:
                with open("text.txt", "a", encoding="utf-8") as inf_build:
                    inf_build.write(f"\n\nЛюди в доме: {self.people_in_house}; \nГод зарегестрированного дома: {self.year}; \nГород: {self.city}; \nКачество ремонта: {self.repair};")
                    print("*Данные добавлены")
            else:
                with open("text.txt", "w", encoding="utf-8") as inf_build:
                    inf_build.write(f"Люди в доме: {self.people_in_house}; \nГод зарегестрированного дома: {self.year}; \nГород: {self.city}; \nКачество ремонта: {self.repair};")
                    print("*Данные записаны")





year = int(input("Год: "))
people_in_house = int(input("Люди в доме: "))
city = input("Город: ")
repair = input("Качество ремонта: ")
house = House(year, city, people_in_house, repair)
house.get_info()