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

        self.units = [Constants.m]*dim
        self.lower_limits = [Constants.ninfinity]*dim
        self.upper_limtis = [Constants.infinity]*dim
        self.configuration = np.zeros([dim, 1])

    def set_units(self, units):

        for i, el in enumerate(units):
            self.units[i] = el

    def set_configuration(self, configuration):

        for i, el in enumerate(configuration):
            self.configuration[i] = el

    def set_lower_limits(self, lower_limits):

        for i, el in enumerate(lower_limits):
            self.lower_limits[i] = el

    def set_upper_limits(self, upper_limtis):

        for i, el in enumerate(upper_limtis):
            self.upper_limtis[i] = el

    def clip(self):

        self.configuration = Operations.clip_bound(
            self.configuration, self.lower_limits, self.upper_limtis)
