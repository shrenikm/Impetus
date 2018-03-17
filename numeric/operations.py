import numpy as np
import math

from constants import Constants

# Class to implement mathematical operations.

class Operations(Constants):

    def __init__(self):
        pass

    @classmethod
    def rad2deg(cls, angle):

        return math.degrees(angle)

    @classmethod
    def deg2rad(cls, angle):

        return math.radians(angle)

    @classmethod
    def normalize_vector(cls, v):

        return v/math.sqrt(np.sum(v*v))
