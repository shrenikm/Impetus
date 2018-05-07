import numpy as np

from rotation import Rotation
from .. numeric.constants import Constants
from .. numeric.operations import Operations

# Class that implements operations related to rotation matrices.


class RotMat(Rotation):

    def __init__(self):

        super(RotMat, self).__init__()

    @classmethod
    def gen_rm_single_frame(cls, frame):

        r = np.zeros([3, 3])
        r[0, :] = frame.x.T
        r[1, :] = frame.y.T
        r[2, :] = frame.z.T

        return r

    @classmethod
    def gen_rm_all_frame(cls, frame):

        r = RotMat.gen_rm_single_frame(frame)
        tmp_frame = frame

        while tmp_frame.base is not None:

            r = np.dot(RotMat.gen_rm_single_frame(tmp_frame.base), r)
            tmp_frame = tmp_frame.base

        return r

    @classmethod
    def gen_rm_rotframe(cls, frame_start, frame_end):

        r_start = RotMat.gen_rm_all_frame(frame_start)
        r_end = RotMat.gen_rm_all_frame(frame_end)
        return np.dot(r_start, r_end.T)

    def gen_rmx(self, angle):

        r = np.zeros([3, 3])
        r[0, 0] = 1

        r[1, 1] = np.cos(angle)
        r[1, 2] = -np.sin(angle)
        r[2, 1] = np.sin(angle)
        r[2, 2] = np.cos(angle)

        return r

    def gen_rmy(self, angle):

        r = np.zeros([3, 3])
        r[1, 1] = 1

        r[0, 0] = np.cos(angle)
        r[0, 2] = np.sin(angle)
        r[2, 0] = -np.sin(angle)
        r[2, 2] = np.cos(angle)

        return r

    def gen_rmz(self, angle):

        r = np.zeros([3, 3])
        r[2, 2] = 1

        r[0, 0] = np.cos(angle)
        r[0, 1] = -np.sin(angle)
        r[1, 0] = np.sin(angle)
        r[1, 1] = np.cos(angle)

        return r

    # Euler angle rotation matrices.

    def gen_euler_rm(self, angles, seq):

        pass
