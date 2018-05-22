import numpy as np
import math

# Class to store constants for the library.

class Physical(object):

    # Physical constants
    #TODO: Make these more accurate
    g = 9.81

class Units(object):

    # Impetus type constants
    deg, rad = 'deg', 'rad'
    m, mm, cm = 'm', 'mm', 'cm'
    infinity = "infinity"
    ninfinity = "ninfinity"

class Struct(object):

    # Axis constants
    gx = {'ax': 'x', 'type': 'global'}
    gy = {'ax': 'y', 'type': 'global'}
    gy = {'ax': 'z', 'type': 'global'}
    lx = {'ax': 'x', 'type': 'local'}
    ly = {'ax': 'y', 'type': 'local'}
    lz = {'ax': 'z', 'type': 'local'}

class Matrices(object):

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


class Colors(object):

    #Floating point
    red_f = [1.0, 0.0, 0.0, 1.0]
    green_f = [0.0, 1.0, 0.0, 1.0]
    blue_f = [0.0, 0.0, 1.0, 1.0]

    #Integer
    red_d = [255, 0, 0, 255]
    green_d = [0, 255, 0, 255]
    blue_d = [0, 0, 255, 255]


class RenderObjects(object):

    frame = "Frame"
    vector = "Vector"
    sphere = "Sphere"
    cube = "Cube"
    cuboid = "Cuboid"
    cylinder = "Cylinder"






















