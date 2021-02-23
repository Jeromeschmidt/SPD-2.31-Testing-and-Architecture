import pytest

import math

def display_grade_stat():
    """Gathers stats and print them out."""
    grade_list = read_input()
    # Calculate the mean and standard deviation of the grades
    mean, standard_deviation = calculate_stat(grade_list)
    # print out the mean and standard deviation in a nice format.
    print_stat(mean, standard_deviation)

def read_input():
    """Get the inputs from the user."""
    grade_list = []
    n_student = 5
    for _ in range(0, n_student):
        grade_list.append(int(input('Enter a number: ')))
    return grade_list

def calculate_stat(grade_list):
    """Calculate the mean and standard deviation of the grades."""
    if grade_list == []:
        raise ValueError
    total = 0
    for grade in grade_list:
        total = total + grade
    mean = total / len(grade_list)
    sum_of_sqrs = 0
    for grade in grade_list:
        sum_of_sqrs += (grade - mean) ** 2
    sd = math.sqrt(sum_of_sqrs / len(grade_list)) # standard deviation
    return mean, sd

def print_stat(mean, sd):
    """print out the mean and standard deviation in a nice format."""
    print('****** Grade Statistics ******')
    print("The grades's mean is:", mean)
    print('The population standard deviation of grades is: ', round(sd, 3))
    print('****** END ******')

# display_grade_stat()
#
# def test_read_input():
#     pass

#
# def test_display_grade_stat():
#     pass

def test_calculate_stat():
    grade_list = [1,2,3,4,5]
    mean, sd = calculate_stat(grade_list)
    assert mean == 3
    assert round(sd, 3) == 1.414

    with pytest.raises(ValueError):
        calculate_stat([])


def test_print_stat(capfd):
    print_stat(3, 1.414)
    out,err=capfd.readouterr()
    assert out == "****** Grade Statistics ******\nThe grades's mean is: 3\nThe population standard deviation of grades is:  1.414\n****** END ******\n"
