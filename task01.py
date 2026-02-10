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
        self.records:dict = {}

    def add_record(self, championship_name:str, rank:int)->None:
        if (not championship_name or rank < 1):
            raise ValueError
        if (championship_name not in self.records.keys()):
            self.records[championship_name] = rank


    def print(self):
        print(f"My name is {self.name}, from {self.country}.\nMy birth date is {self.birthdate}.")
        if not self.records:
            return
        print("My records are:")
        for i in sorted(self.records.keys()):
            print(f"Rank {self.records[i]} at the {i}")
