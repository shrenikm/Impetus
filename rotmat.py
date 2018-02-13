import numpy as np

from rotation import Rotation
from numerical import Constants
from numerical import Operations

# Class that implements operations related to rotation matrices.


class RotMat(Rotation, Operations):

    def __init__(self, units='rad'):

        super(RotMat, self).__init__(units)

    def get_units(self):

        return super(RotMat, self).get_units()

    def set_units(self, units):

        super(RotMat, self).set_units(units)

    def gen_rm_single_frame(self, frame):

        r = np.zeros([3, 3])
        r[0, :] = frame.x.T
        r[1, :] = frame.y.T
        r[2, :] = frame.z.T

        return r

    def gen_rm_all_frame(self, frame):

        r = self.gen_rm_single_frame(frame)
        frame_tmp = frame

        while frame_tmp.base is not None:

            r = np.dot(self.gen_rm_single_frame(frame_tmp.base), r)
            frame_tmp = frame_tmp.base

        return r

    def gen_rm_rotframe(self, frame_start, frame_end=None):

        if frame_end is None:
            return self.gen_rm_all_frame(frame_start)

        r_start = self.gen_rm_all_frame(frame_start)
        r_end = self.gen_rm_all_frame(frame_end)
        return np.dot(r_start.T, r_end)

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

    # Euler angle rotation matrices.

    def gen_euler_rm(self, angles, seq):

        pass
