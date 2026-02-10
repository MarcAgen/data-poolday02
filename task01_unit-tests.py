##
## EPITECH PROJECT, 2026
## day02
## File description:
## task01_unit-tests
##
import unittest as test
from contextlib import redirect_stdout
from task01 import Athlete

class TestAthlete(test.TestCase):
    def test_base_infos(self):
        athlete = Athlete("mkleo", "Mexico", "2O/01/2001")
        self.assertEqual(athlete.name, "mkleo")
        self.assertEqual(athlete.country, "Mexico")
        self.assertEqual(athlete.birthdate, "20/01/2001")

    def test_record_adding(self):
        athlete = Athlete("mkleo", "Mexico", "2O/01/2001")
        athlete.add_record("lets make big moves", 5)
        self.assertEqual(athlete.records[0]["championship name"], "lets make big moves")
        self.assertEqual(athlete.records[0]["rank"], 5)
    
    def test_record_overwrite(self):
        athlete = Athlete("mkleo", "Mexico", "2O/01/2001")
        athlete.add_record("lets make big moves", 5)
        athlete.add_record("lets make big moves", 1)
        self.assertEqual(athlete.records[0]["rank"], 1)
    
    def test_print_no_record(self):
        athlete = Athlete("mkleo", "Mexico", "2O/01/2001")
        athlete.print()
    
    def test_print_single_record(self):
        athlete = Athlete("mkleo", "Mexico", "2O/01/2001")
        athlete.add_record("lets make big moves", 5)
        athlete.print()

    def test_print_single_record(self):
        athlete = Athlete("mkleo", "Mexico", "2O/01/2001")
        athlete.add_record("lets make big moves", 5)
        athlete.add_record("Ragnarok: Origin", 1)
        athlete.print()

if __name__ == " __main__ " :
    test.main()
