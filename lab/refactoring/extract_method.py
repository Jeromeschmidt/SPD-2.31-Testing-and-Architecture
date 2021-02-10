# Written by Kamran Bigdely
# Example for Compose Methods: Extract Method.
"""
Methods for calculating mean and standard deviation of a class's grade
"""
import math

def get_grades():
    """Gets the grades for the class from user"""
    grade_list = []
    # Get the inputs from the user
    n_student = 5
    for _ in range(0, n_student):
        grade_list.append(int(input('Enter a number: ')))

    return grade_list

def get_mean(grade_list):
    """Calculate the mean of the grades"""
    suma = 0 # Do you think 'sum' is a good var name? Run pylint to figure out!
    for grade in grade_list:
        suma = suma + grade
    mean = suma / len(grade_list)

    return mean


def get_sd(mean, grade_list):
    """Calculate the standard deviation of the grades"""
    stan_dev = 0 # standard deviation
    sum_of_sqrs = 0
    for grade in grade_list:
        sum_of_sqrs += (grade - mean) ** 2
    stan_dev = math.sqrt(sum_of_sqrs / len(grade_list))
    return stan_dev

def print_results(mean, stan_dev):
    """print out the mean and standard deviation in a nice format."""
    print('****** Grade Statistics ******')
    print("The grades's mean is:", mean)
    print('The population standard deviation of grades is: ', round(stan_dev, 3))
    print('****** END ******')

def print_stat():
    """Gets the mean and standard deviation of a class scores and prints them out"""

    grade_list = get_grades()

    mean = get_mean(grade_list)

    stan_dev = get_sd(mean, grade_list)

    print_results(mean, stan_dev)

print_stat()
