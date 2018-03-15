import numpy as np
import math

# Class to store constants for the library.


class Constants(object):

    # Mathematical constants
    pi = np.pi
    e = np.e

    # Impetus type constants
    deg, rad = 'deg', 'rad'
    m, mm, cm = 'm', 'mm', 'cm'

    # Axis constants
    gx, gy, gz, lx, ly, lz = 'X', 'Y', 'Z', 'x', 'y', 'z'
    std_axis_x = np.array([[1], [0], [0]])
    std_axis_y = np.array([[0], [1], [0]])
    std_axis_z = np.array([[0], [0], [1]])
    std_origin = np.array([[0], [0], [0]])

