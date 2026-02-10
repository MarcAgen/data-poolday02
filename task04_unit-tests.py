##
## EPITECH PROJECT, 2026
## day02
## File description:
## task04_unit-tests
##
import unittest as test
from task04 import Athlete, Competition

class TestCompetition(test.TestCase):
    def test_base_infos(self):
        compet = Competition("SmashMania")
        self.assertEqual(compet.name, "SmashMania")
    
    def test_add_athlete(self):
        mkleo = Athlete("mkleo", "Mexico", "2O/01/2001")
        compet = Competition("SmashMania")
        compet.add_athlete(mkleo)
        self.assertEqual(compet.athletes[0]._name, "mkleo")
    
    def test_exclude(self):
        mkleo = Athlete("mkleo", "Mexico", "2O/01/2001")
        bassmage = Athlete("bassmage", "USA", "17/01/2002")
        compet = Competition("SmashMania")
        compet.add_athlete(mkleo)
        compet.add_athlete(bassmage)
        compet.exclude(mkleo)
        self.assertEqual(compet.athletes[0]._name == "bassmage")

    def test_rank(self):
        mkleo = Athlete("mkleo", "Mexico", "2O/01/2001")
        compet = Competition("SmashMania")
        compet.add_athlete(mkleo)
        compet.rank(mkleo, 7)
        self.assertEqual(mkleo._records[0]["rank"], 7)
