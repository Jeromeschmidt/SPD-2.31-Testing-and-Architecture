# by Kami Bigdely
# Inline method.
<<<<<<< HEAD
"""Finds out if a person should be allowed to enter or not based on age"""
=======
# TODO: Refactor this program to improve its readability.

>>>>>>> d2def69c32b08225c735678af9af6c112aa73233
LEGAL_DRINKING_AGE = 18

class Person:
    """Person class for holding a persons identity"""
    def __init__(self, my_age):
        self.age = my_age

def enter_night_club(individual):
    """Determines if a person should be allowed to enter or not based on age"""
    if individual.age > LEGAL_DRINKING_AGE:
        print("Allowed to enter.")
    else:
        print("Enterance of minors is denited.")

person = Person(17.9)
enter_night_club(person)
<<<<<<< HEAD
=======
        
>>>>>>> d2def69c32b08225c735678af9af6c112aa73233
