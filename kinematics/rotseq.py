import numpy as np

from rotation import Rotation
from .. numeric.constants import Constants
from .. numeric.operations import Operations

# Class that implements rotation sequences and bundles them in a list representation.


class RotSeq(Rotation, Operations):

    def __init__(self, angle_units='rad'):

        super(RotSeq, self).__init__(angle_units)
        self.sequence = [[], []]

    def get_units(self):

        return super(RotSeq, self).get_angle_units()

    def set_units(self, angle_units):

        super(RotSeq, self).set_angle_units(angle_units)

    def add_rotation(self, angles, axes):
        angles = self.conv_angles(angles)
        self.sequence[0] += axes
        self.sequence[1] += angles
        pass
