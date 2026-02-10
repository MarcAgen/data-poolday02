##
## EPITECH PROJECT, 2026
## day02
## File description:
## task01
##

class Athlete:
    def __init__(self, name:str, country:str, birthdate:str)->None:
        self._name:str = name
        self._country:str = country
        self._birthdate:str = birthdate
        self._records:list[dict[str, int]]


    def add_record(self, championship_name:str, rank:int)->None:
        if (not championship_name or rank < 1):
            raise ValueError
        for i in self._records:
            if (i["championship name"] == championship_name):
                i["rank"] = rank
                return
        self._records.append({"championship name": championship_name, "rank": rank})


    def print(self):
        print(f"My name is {self._name}, from {self._country}.\nMy birth date is {self._birthdate}.")
        if not self._records:
            return
        print("My records are:")
        for i in self._records:
            print(f"Rank {i["rank"]} at the {i["championship name"]}")
