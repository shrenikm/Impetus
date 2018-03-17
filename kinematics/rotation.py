from abc import ABCMeta, abstractmethod

import numpy as np
from math import sin
from math import cos
from math import pi

from .. numeric.constants import Constants
from .. numeric.operations import Operations


# Main class that serves as a blueprint for all rotation related functions.
# Objects of the Rotation class cannot be created.


class Rotation(object):

    __metaclass__ = ABCMeta

    def __init__(self, angle_units='rad'):
        self.angle_units = angle_units

    @abstractmethod
    def get_angle_units(self):

        return self.angle_units

    @abstractmethod
    def set_angle_units(self, angle_units):

        self.angle_units = angle_units

    def conv_angle(self, angle):

        if (self.angle_units == Constants.deg):
            angle = Operations.deg2rad(angle)
        return angle

    def conv_angles(self, angles):

        if (self.angle_units == Constants.deg):
            angles = [Operations.deg2rad(angles[i])
                      for i in range(len(angles))]
        return angles
