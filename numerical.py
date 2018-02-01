from abc import ABCMeta, abstractmethod

import numpy as np 
import math

#Class to store constants for the library

class Constants(object):


    #Mathematical constants
    pi = np.pi
    e = np.e

    #Impetus type constants
    DEG, RAD = 'deg', 'rad'
    GX, GY, GZ, LX, LY, LZ = 'X', 'Y', 'Z', 'x', 'y', 'z'

#Class to implement mathematical operations

class Operations(Constants):


    def __init__(self):
        pass

    @classmethod
    def rad2deg(cls, angle):

        return math.degrees(angle)

    @classmethod
    def deg2rad(cls, angle):

        return math.radians(angle)





