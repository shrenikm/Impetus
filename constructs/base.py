import numpy as np

from .. numeric.constants import Constants
from .. numeric.operations import Operations
from .. kinematics.rotmat import RotMat
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
        self.x = Operations.normalize_vector(x)
        self.y = Operations.normalize_vector(y)
        self.z = Operations.normalize_vector(z)
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

    def __init__(self, x=0, y=0, z=0, dist_units=Constants.m, base_frame=Frame()):

        self.base_frame = base_frame
        self.x = x
        self.y = y
        self.z = z

    def get_dist_units(self):

        return self.dist_units

    def set_dist_untis(self, dist_units):

        self.dist_units = dist_units

    def get_vector(self):

        return np.array([[self.x], [self.y], [self.z]])

    def get_vector_hom(self):

        return np.concatenate((self.get_vector(), np.array([[1]])), axis=0)

    def compute_world_vector(self):

        rm = RotMat.gen_rm_all_frame(self.base_frame)
        return np.dot(rm, self.get_vector())


class Configuration(Constants):

    def __init__(self, dim=3):

        self.dim = dim
        self.units = [Constants.m]*self.dim
        self.lower_limits = [Constants.ninfinity]*self.dim
        self.upper_limits = [Constants.infinity]*self.dim
        self.value = np.zeros([self.dim, 1])

    def set_units(self, units):

        for i, el in enumerate(units):
            self.units[i] = el

    def set_value(self, configuration):

        for i, el in enumerate(configuration):
            self.value[i] = el

    def set_lower_limits(self, lower_limits):

        for i, el in enumerate(lower_limits):
            self.lower_limits[i] = el

    def get_lower_limits_arr(self):

        return np.array(self.lower_limits).reshape(self.dim, 1)

    def set_upper_limits(self, upper_limits):

        for i, el in enumerate(upper_limits):
            self.upper_limits[i] = el

    def get_upper_limits_arr(self):

        return np.array(self.upper_limits).reshape(self.dim, 1)

    def clip(self):

        self.value = Operations.clip_bound(
            self.value, self.lower_limits, self.upper_limits)
