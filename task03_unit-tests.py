##
## EPITECH PROJECT, 2026
## day02
## File description:
## task03_unit-tests
##
import unittest as test
from task03 import Athlete

class TestAthleteSetter(test.TestCase):
    def test_modified_infos(self):
        athlete = Athlete("mkleo", "Mexico", "2O/01/2001")
        athlete.setName("Bassmage")
        athlete.setCountry("USA")
        athlete.setBirthdate("17/01/2002")
        self.assertEqual(athlete.name, "Bassmage")
        self.assertEqual(athlete.country, "USA")
        self.assertEqual(athlete.birthdate, "17/01/2002")

if __name__ == " __main__ " :
    test.main()
