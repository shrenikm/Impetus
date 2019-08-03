import numpy as np
import math

from Impetus.kinematics.rotation import Rotation
from Impetus.numeric.constants import Physical, Units, Struct, Matrices, RenderObjects
from Impetus.numeric.operations import Operations

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

    @classmethod
    def gen_rmx(cls, angle):

        r = np.zeros([3, 3])
        r[0, 0] = 1.0

        r[1, 1] = np.cos(angle)
        r[1, 2] = -np.sin(angle)
        r[2, 1] = np.sin(angle)
        r[2, 2] = np.cos(angle)

        return r

    @classmethod
    def gen_rmy(cls, angle):

        r = np.zeros([3, 3])
        r[1, 1] = 1.0

        r[0, 0] = np.cos(angle)
        r[0, 2] = np.sin(angle)
        r[2, 0] = -np.sin(angle)
        r[2, 2] = np.cos(angle)

        return r

    @classmethod
    def gen_rmz(cls, angle):

        r = np.zeros([3, 3])
        r[2, 2] = 1.0

        r[0, 0] = np.cos(angle)
        r[0, 1] = -np.sin(angle)
        r[1, 0] = np.sin(angle)
        r[1, 1] = np.cos(angle)

        return r

    @classmethod
    def gen_rm(cls, axis, angle):

        r = np.zeros([3, 3])

        if axis == 'x':
            r = RotMat.gen_rmx(angle)
        if axis == 'y':
            r = RotMat.gen_rmy(angle)
        if axis == 'z':
            r = RotMat.gen_rmz(angle)

        return r


    # Euler angle rotation matrices.
    #Use rotseq for now. Separate euler angle function seems to be redundant

    def gen_rm_euler(self, angles, seq):

        pass
