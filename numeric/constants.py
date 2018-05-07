import numpy as np
import math

# Class to store constants for the library.


class Constants(object):

    # Mathematical constants
    pi = np.pi
    e = np.e

    # Physical constants
    #TODO: Make these more accurate
    g = 9.81

    # Impetus type constants
    deg, rad = 'deg', 'rad'
    m, mm, cm = 'm', 'mm', 'cm'
    infinity = "infinity"
    ninfinity = "ninfinity"

    # Axis constants
    gx, gy, gz, lx, ly, lz = 'X', 'Y', 'Z', 'x', 'y', 'z'

    std_axis_x = np.array([[1], [0], [0]])
    std_axis_y = np.array([[0], [1], [0]])
    std_axis_z = np.array([[0], [0], [1]])
    std_origin = np.array([[0], [0], [0]])

    vector_zero = np.array([[0], [0], [0]])
    vector_zero_hom = np.array([[0], [0], [0], [1]])

    vector_one = np.array([[1], [1], [1]])
    vector_one_hom = np.array([[1], [1], [1], [1]])

    mat3_zero = np.zeros([3, 3])
    mat4_zero = np.zeros([4, 4])


