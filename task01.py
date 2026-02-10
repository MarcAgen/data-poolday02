##
## EPITECH PROJECT, 2026
## day02
## File description:
## task01
##

class Athlete:
    def __init__(self, name:str, country:str, birthdate:str)->None:
        self.name:str = name
        self.country:str = country
        self.birthdate:str = birthdate
        self.records:list[dict[str, int]]
    

    def add_record(self, championship_name:str, rank:int)->None:
        if (not championship_name or rank < 1):
            raise ValueError
        for i in self.records:
            if (i["championship name"] == championship_name):
                i["rank"] = rank
                return
        self.records.append({"championship name": championship_name, "rank": rank})


    def print(self):
        print(f"My name is {self.name}, from {self.country}.\nMy birth date is {self.birthdate}.")
        if not self.records:
            return
        print("My records are:")
        for i in self.records:
            print(f"Rank {i["rank"]} at the {i["championship name"]}")
