import numpy as np

from transformation import Transformation
from .. numeric.constants import Constants
from .. numeric.operations import Operations

# Class that implements operations related to rotation matrices.


class TfMat(Transformation, Operations):

    def __init__(self, angle_units='rad', dist_units = 'm'):

        super(TfMat, self).__init__(angle_units, dist_units)

    def get_angle_units(self):

        return super(TfMat, self).get_angle_units()

    def get_dist_units(self):

        return super(TfMat, self).get_dist_units()

    def set_angle_units(self, angle_units):

        super(TfMat, self).set_angle_units(angle_units)

    def set_dist_units(self, dist_units):

        super(TfMat, self).set_dist_units(dist_units)

    # def gen_rm_single_frame(self, frame):

    #     r = np.zeros([3, 3])
    #     r[0, :] = frame.x.T
    #     r[1, :] = frame.y.T
    #     r[2, :] = frame.z.T

    #     return r

    # def gen_rm_all_frame(self, frame):

    #     r = self.gen_rm_single_frame(frame)
    #     frame_tmp = frame

    #     while frame_tmp.base is not None:

    #         r = np.dot(self.gen_rm_single_frame(frame_tmp.base), r)
    #         frame_tmp = frame_tmp.base

    #     return r

    # def gen_rm_rotframe(self, frame_start, frame_end=None):

    #     if frame_end is None:
    #         return self.gen_rm_all_frame(frame_start)

    #     r_start = self.gen_rm_all_frame(frame_start)
    #     r_end = self.gen_rm_all_frame(frame_end)
    #     return np.dot(r_start.T, r_end)

    # def gen_rmx(self, angle):

    #     r = np.zeros([3, 3])
    #     r[0, 0] = 1

    #     angle = self.conv_angle(angle)

    #     r[1, 1] = np.cos(angle)
    #     r[1, 2] = -np.sin(angle)
    #     r[2, 1] = np.sin(angle)
    #     r[2, 2] = np.cos(angle)

    #     return r

    # def gen_rmy(self, angle):

    #     r = np.zeros([3, 3])
    #     r[1, 1] = 1

    #     angle = self.conv_angle(angle)

    #     r[0, 0] = np.cos(angle)
    #     r[0, 2] = np.sin(angle)
    #     r[2, 0] = -np.sin(angle)
    #     r[2, 2] = np.cos(angle)

    #     return r

    # def gen_rmz(self, angle):

    #     r = np.zeros([3, 3])
    #     r[2, 2] = 1

    #     angle = self.conv_angle(angle)

    #     r[0, 0] = np.cos(angle)
    #     r[0, 1] = -np.sin(angle)
    #     r[1, 0] = np.sin(angle)
    #     r[1, 1] = np.cos(angle)

    #     return r

    # # Euler angle rotation matrices.

    # def gen_euler_rm(self, angles, seq):

    #     pass
