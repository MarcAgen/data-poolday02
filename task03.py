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
        self._records:dict = {}

    def add_record(self, championship_name:str, rank:int)->None:
        if (not championship_name or rank < 1):
            raise ValueError
        if (championship_name not in self._records.keys()):
            self._records[championship_name] = rank

    def print(self):
        print(f"My name is {self._name}, from {self._country}.\nMy birth date is {self._birthdate}.")
        if not self._records:
            return
        print("My records are:")
        for i in sorted(self._records.keys()):
            print(f"Rank {self._records[i]} at the {i}")

    def setName(self, new_name:str):
        if not new_name:
            raise ValueError
        self._name = new_name

    def setCountry(self, new_country:str):
        if not new_country:
            raise ValueError
        self._country = new_country

    def setBirthdate(self, new_birthdate:str):
        if not new_birthdate:
            raise ValueError
        self._birthdate = new_birthdate
