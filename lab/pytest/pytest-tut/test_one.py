import math

def calculate_kinetic_energy(mass, velocity):
    """Returns kinetic energy of mass [kg] with velocity [ms]."""
    return 0.5 * mass * velocity ** 2

# def calculate_kinetic_energy(mass, velocity):
#     """Returns kinetic energy of mass [kg] with velocity [ms]."""
#     return mass * velocity ** 2


def test_calculate_kinetic_energy():
    mass = 10 # [kg]
    velocity = 4 # [m/s]
    assert calculate_kinetic_energy(mass, velocity) == 80


def get_average(li):
    if li == []:
        return float('NaN')
    sum = 0
    for num in li:
        sum += num
    mean = sum / len(li)
    return mean

def test_get_average():
    nums = [1,2,3,4]
    assert get_average(nums) == 2.5
    assert math.isnan(get_average([]))
