##
## EPITECH PROJECT, 2026
## day02
## File description:
## task04
##
from task03 import Athlete

class Competition:
    def __init__(self, name:str)->None:
        self.name:str = name
        self.athletes:list[Athlete] = []

    def add_athlete(self, athlete:Athlete)->None:
        if not isinstance(athlete, Athlete):
            raise ValueError
        for i in self.athletes:
            if i._name == athlete._name:
                return
        self.athletes.append(athlete)

    def exclude(self, athlete:Athlete)->None:
        for i in range(len(self.athletes)):
            if self.athletes[i] == athlete._name:
                self.athletes.remove(athlete)

    
    def rank(self, athlete:Athlete, rank:int)->None:
        if rank < 1:
            raise ValueError
        for i in self.athletes:
            if i._name == athlete._name:
                athlete.add_record(self.name, rank)
                return
        
        raise ValueError

    def print(self)->None:
        if not self.athletes:
            print(f"The {self.name} has no athlete.")
        else:
            print(f"{len(self.athletes)} athlete(s)engaged in the {self.name}:")
            for i in sorted(self.athletes, key=lambda x: x._name, reverse=False):
                print(f"{i._name} ({i._birthdate})from {i._country}")
