import numpy as np
import math

from Impetus.kinematics.rotation import Rotation
from Impetus.kinematics.rotmat import RotMat
from Impetus.numeric.constants import Physical, Units, Struct, Matrices, RenderObjects
from Impetus.numeric.operations import Operations
from Impetus.constructs.base import Axis

# Class that implements rotation sequences and bundles them in a list representation.


class RotSeq(Rotation):

    def __init__(self):

        super(RotSeq, self).__init__()
        self.sequence = [[], []]
        

    def add_rotation(self, axes, angles):

        self.sequence[0] += axes
        self.sequence[1] += angles
        
    def gen_rm(self):

        r = np.eye(3)

        for i in range(len(self.sequence[0])):

            ax = self.sequence[0][i]['ax']
            ty = self.sequence[0][i]['type']
            angle = self.sequence[1][i]

            rm = RotMat.gen_rm(ax, angle)

            if ty == 'local':

                r = np.dot(rm, r)

            if ty == 'global':

                r = np.dot(r, rm)

        return r

            




