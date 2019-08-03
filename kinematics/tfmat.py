import numpy as np
import math

from Impetus.constructs.base import Frame
from Impetus.kinematics.rotmat import RotMat
from Impetus.kinematics.transformation import Transformation
from Impetus.numeric.constants import Physical, Units, Struct, Matrices, RenderObjects
from Impetus.numeric.operations import Operations

# Class that implements operations related to rotation matrices.

#All angles must be in radians and all distances in meters


class TfMat(Transformation):


    def __init__(self):

        super(TfMat, self).__init__()


    @classmethod
    def gen_tm_from_rot(cls, rm, d=Matrices.vector_zero):

        t = np.concatenate((np.concatenate((rm, d), axis=1),
                            Matrices.vector_zero_hom.T), axis=0)

        return t

    @classmethod
    def gen_tm_single_frame(cls, frame):

        r = np.zeros([3, 3])
        r[0, :] = frame.x.T
        r[1, :] = frame.y.T
        r[2, :] = frame.z.T

        return cls.gen_tm_from_rot(r, frame.origin)

    @classmethod
    def gen_tm_all_frame(cls, frame):


        rm = self.rotmat.gen_rm_single_frame(frame)
        frame_tmp = frame

        while frame_tmp.base is not None:

            r = np.dot(RotMat.gen_rm_single_frame(frame_tmp.base), rm)
            frame_tmp = frame_tmp.base

        return cls.gen_tm_from_rot(rm, frame.compute_world_origin())

    @classmethod
    def gen_tm_rotframe(cls, frame_start, frame_end):


        rm_start = RotMat.gen_rm_all_frame(frame_start)
        rm_end = RotMat.gen_rm_all_frame(frame_end)
        rm = np.dot(rm_start.T, rm_end)

        return cls.gen_tm_from_rot(rm, frame_end.compute_world_origin() - frame_start.compute_world_origin())

    @classmethod
    def invert(cls, tm):

        rm = tm[0:3, 0:3]
        d = tmp[3, 0:3]
        return np.concatenate((np.concatenate((rm.T, -np.dot(rm.T, d)), axis = 1)), axis = 0)
