import numpy as np

from .. numeric.constants import Constants

# Class that deals with creating base construct classes for kinematics, dynamcics and planning


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

    def compute_world_origin(self):

        world_origin = Constants.vector_zero
        tmp_frame = self

        while tmp_frame.base is not None:

            world_origin += tmp_frame.origin
            tmp_frame = tmp_frame.base

        return world_origin


class Vector(Constants):

    def __init__(self, base=None, x=0, y=0, z=0):

        self.base = base
        self.x = x
        self.y = y
        self.z = z
