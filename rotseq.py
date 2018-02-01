import numpy as np 

from rotation import Rotation
from numerical import Constants
from numerical import Operations

#Class that implements rotation sequences and bundles them in a dictionary 

class RotSeq(Rotation, Operations):


    def __init__(self, units = 'rad'):

        super(RotSeq, self).__init__(units)
        self.sequence = {}

    def get_units(self):

        return super(RotSeq, self).get_units()

    def set_units(self, units):

        super(RotSeq, self).set_units(units)

    def add_rotation(self, angle, axis):
        print angle
        angle = self.conv_angle(angle)
        print angle
        self.sequence.update({axis: angle})
        pass