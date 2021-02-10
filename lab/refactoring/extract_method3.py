# Written by Kamran Bigdely, refractored by Jerome Schmidt
# Example for Compose Methods: Extract Method.
"""
Methods for calculating distance and length
"""
import math


def calcualte_distance(x_1, x_2, y_1, y_2):
    """Calculate the distance between the two circle."""
    distance = math.sqrt((x_1-x_2)**2 + (y_1 - y_2)**2)
    print('distance', distance)

def calcualte_length(x_1, x_2, y_1, y_2):
    """calcualte the length of vector AB vector which is a vector between A and B points."""
    length = math.sqrt((x_1-x_2)*(x_1-x_2) + (y_1-y_2)*(y_1-y_2))
    print('length', length)

calcualte_distance(4, 53, 4.25, -5.35)

calcualte_length(-36, .34, 97, .91)
