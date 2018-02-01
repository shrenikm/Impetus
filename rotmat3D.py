import numpy as np 

from rotation import Rotation
from numerical import Constants
from numerical import Operations

#Class that implements operations related to rotation matrices

class RotMat3D(Rotation, Operations):


    def __init__(self, units = 'rad'):

        super(RotMat3D, self).__init__(units)
        
    def get_units(self):

        return super(RotMat3D, self).get_units()

    def set_units(self, units):

        super(RotMat3D, self).set_units(units)

    #The rotation matrices for simple single angle rotations about the x, y or z axes

    def gen_rmx(self, angle):

        r = np.zeros([3, 3])
        r[0, 0] = 1

        angle = self.conv_angle(angle)

        r[1, 1] = np.cos(angle)
        r[1, 2] = -np.sin(angle)
        r[2, 1] = np.sin(angle)
        r[2, 2] = np.cos(angle)

        return r

    def gen_rmy(self, angle):

        r = np.zeros([3, 3])
        r[1, 1] = 1

        angle = self.conv_angle(angle)

        r[0, 0] = np.cos(angle)
        r[0, 2] = np.sin(angle)
        r[2, 0] = -np.sin(angle)
        r[2, 2] = np.cos(angle)

        return r

    def gen_rmz(self, angle):

        r = np.zeros([3, 3])
        r[2, 2] = 1

        angle = self.conv_angle(angle)

        r[0, 0] = np.cos(angle)
        r[0, 1] = -np.sin(angle)
        r[1, 0] = np.sin(angle)
        r[1, 1] = np.cos(angle)

        return r

    #Euler angle rotation matrices

    def gen_euler_rm(self, angles, seq):

        pass





