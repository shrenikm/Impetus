import numpy as np

from rotation import Rotation
from .. numeric.constants import Constants
from .. numeric.operations import Operations
from .. constructs.base import Axis

# Class that implements rotation sequences and bundles them in a list representation.


class RotSeq(Rotation):

    def __init__(self):

        super(RotSeq, self).__init__()
        self.sequence = [[], []]
        

    def add_rotation(self, axes, angles):

        self.sequence[0] += axes
        self.sequence[1] += angles
        pass
