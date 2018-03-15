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

    def __init__(self, units='rad'):
        self.units = units

    @abstractmethod
    def get_units(self):

        return self.units

    @abstractmethod
    def set_units(self, units):

        self.units = units

    def conv_angle(self, angle):

        if (self.units == Constants.deg):
            angle = Operations.deg2rad(angle)
        return angle

    def conv_angles(self, angles):

        if (self.units == Constants.deg):
            angles = [Operations.deg2rad(angles[i])
                      for i in range(len(angles))]
        return angles
