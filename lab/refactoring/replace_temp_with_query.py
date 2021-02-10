<<<<<<< HEAD
# Adapted from a Java code in the "Refactoring" book by Martin Fowler.
# Replace temp with query
# Code snippet. Not runnable.
"""
Gets price of an order based on item_price and quantity
"""

def get_price(quantity, item_price):
    """Gets total price for an order"""
    base_price = quantity * item_price
    discount_factor = get_dis_factor(item_price)

    return base_price * discount_factor

def get_dis_factor(base_price):
    """Gets discount factor based on price"""
    if base_price > 1000:
        return 0.95
    return 0.98

print(get_price(5, 10))
=======
# By Kamran Bigdely Nov. 2020
# Replace temp variable with query
# TODO: Use 'extract method' refactoring technique to improve this code. If required, use
#       'replace temp variable with query' technique to make it easier to extract methods.
class Employer:    
    def __init__(self, name):
        self.name = name
    def send(self, students):
        print("Students' contact info were sent to", self.name + '.')

class Student:
    def __init__(self, gpa, name):
        self.gpa = gpa
        self.name = name
    def get_gpa(self):
        return self.gpa
    def send_congrat_email(self):
        print("Congrats", self.name + ". You graduated successfully!")

class School:
    def __init__(self, students) -> None:
        self.students = students
    def process_graduation(self):
        # Find the students in the school who have successfully graduated.
        min_gpa = 2.5 # minimum acceptable GPA
        passed_students = []
        for s in self.students:
            if s.get_gpa() > min_gpa:
                passed_students.append(s)

        # print student's name who graduated.
        print('*** Student who graduated *** ')
        for s in passed_students:
            print(s.name)
        print('****************************')
        # Send congrat emails to them.
        for s in passed_students:
            s.send_congrat_email()
        # Find the top 10% of them and send their contact to the top employers
        passed_students.sort(key=lambda s: s.get_gpa())
        percentile = 0.9
        index = int(percentile * len(passed_students))
        top_10_percent = passed_students[index:]
        top_employers = [Employer('Microsoft'), Employer('Free Software Foundation'), Employer('Google')]
        for e in top_employers:
            e.send(top_10_percent)

students = [Student(2.1, 'donald'), Student(2.3, 'william'), Student(2.7, 'toro'), 
            Student(3.9, 'lili'), Student(3.2,'kami'), Student(3,'sarah')]
school  = School(students)
school.process_graduation()
>>>>>>> d2def69c32b08225c735678af9af6c112aa73233
