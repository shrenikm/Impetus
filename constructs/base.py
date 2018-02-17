import numpy as np

from numeric.constants import Constants

# Class that deals with creating reference frames.


class Frame(Constants):

    def __init__(
            self, base=None,
            x=Constants.std_axis_x,
            y=Constants.std_axis_y,
            z=Constants.std_axis_z,
            origin=Constants.std_origin,
            is_std=True):

        self.base = base
        self.x = x
        self.y = y
        self.z = z
        self.origin = origin
        self.is_std = is_std


class Vector(Constants):

    def __init__(self, base=None, x=0, y=0, z=0):

        self.base = base
        self.x = x
        self.y = y
        self.z = z


class Axis(Vector, Constants):

    def __init__(self, base=None, x=0, y=0, z=0):

        super(Axis, self).__init__(base, x, y, z)
