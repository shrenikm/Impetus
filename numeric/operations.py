import numpy as np
import math

from constants import Physical, Units, Struct, Matrices, RenderObjects

# Class to implement mathematical operations.

class Operations():

    def __init__(self):
        pass

    @classmethod
    def rad2deg(cls, angle):

        return math.degrees(angle)

    @classmethod 
    def rad2deglist(cls, angles):

        for i in range(len(angles)):
            angles[i]=  math.degrees(angles[i])
        return angles

    @classmethod
    def deg2rad(cls, angle):

        return math.radians(angle)

    @classmethod
    def deg2radlist(cls, angles):

        for i in range(len(angles)):
            angles[i] = math.radians(angles[i])
        return angles


    @classmethod
    def normalize_vector(cls, v):

        return v/math.sqrt(np.sum(v*v))

    @classmethod
    def clip_bound(cls, x, lower, upper):

        for i in range(len(lower)):

            if x[i] < lower[i] and lower[i] != Units.ninfinity:
                x[i] = lower[i]
            if x[i] > upper[i] and upper[i] != Units.infinity:
                x[i] = upper[i]

        return x
