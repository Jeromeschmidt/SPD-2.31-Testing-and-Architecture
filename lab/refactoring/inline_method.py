# by Kami Bigdely
# Inline method.
"""Finds out if a person should be allowed to enter or not based on age"""
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
