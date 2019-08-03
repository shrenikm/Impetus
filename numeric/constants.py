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

    #Floating point with alpha
    red_fa = (1.0, 0.0, 0.0, 1.0)
    green_fa = (0.0, 1.0, 0.0, 1.0)
    blue_fa = (0.0, 0.0, 1.0, 1.0)
    yellow_fa = (1.0, 0.5, 0, 1.0)
    brown_fa = (0.59, 0.29, 0.0, 1.0)

    #Integer with alpha
    red_ia = (255, 0, 0, 255)
    green_ia = (0, 255, 0, 255)
    blue_ia = (0, 0, 255, 255)
    yellow_ia = (255, 127, 0, 255)
    brown_ia = (150, 75, 0, 255)

    #Floating point without alpha
    red_f = red_fa[0:3]
    green_f = green_fa[0:3]
    blue_f = blue_fa[0:3]
    yellow_f = yellow_fa[0:3]
    brown_f = brown_fa[0:3]

    #Integer without alpha
    red_i = red_ia[0:3]
    green_i = green_ia[0:3]
    blue_i = blue_ia[0:3]
    yellow_i = yellow_ia[0:3]
    brown_i = brown_ia[0:3]


class RenderObjects(object):

    frame = "Frame"
    vector = "Vector"
    sphere = "Sphere"
    cube = "Cube"
    cuboid = "Cuboid"
    cylinder = "Cylinder"






















