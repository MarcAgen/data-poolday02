##
## EPITECH PROJECT, 2026
## day02
## File description:
## task06
##
from task03 import Athlete
from task05 import Competition

class SoccerAthlete(Athlete):
    team:str
    post:str

    def print(self):
        super().print()
        print(f"As a soccer player: I am a {self.post} at {self.team}.")

class FighterAthlete(Athlete):
    wins:int = 0
    draw:int = 0
    loss:int = 0

    def print(self):
        super().print()
        print(f"As a fighter athlete: I have {self.wins} wins, {self.draw} draws, {self.loss} loss.")

class MMAFighterAthlete(FighterAthlete):
    organisations:list[str] = []

    def print(self):
        super().print()
        print(f" and I fight MMA in the organizations {self.organisations}")
