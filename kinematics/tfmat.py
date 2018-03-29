import numpy as np

from transformation import Transformation
from .. numeric.constants import Constants
from .. numeric.operations import Operations
from .. constructs.base import Frame
from rotmat import RotMat

# Class that implements operations related to rotation matrices.


class TfMat(Transformation):


    def __init__(self, angle_units='rad', dist_units='m'):

        super(TfMat, self).__init__(angle_units, dist_units)

    def get_angle_units(self):

        return super(TfMat, self).get_angle_units()

    def get_dist_units(self):

        return super(TfMat, self).get_dist_units()

    def set_angle_units(self, angle_units):

        super(TfMat, self).set_angle_units(angle_units)

    def set_dist_units(self, dist_units):

        super(TfMat, self).set_dist_units(dist_units)

    @classmethod
    def gen_tm_from_rot(cls, rm, d=Constants.vector_zero):

        t = np.concatenate((np.concatenate((rm, d), axis=1),
                            Constants.vector_zero_hom.T), axis=0)

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

    def invert(cls, tm):

        rm = tm[0:3, 0:3]
        d = tmp[3, 0:3]
        return np.concatenate((np.concatenate((rm.T, -np.dot(rm.T, d)), axis = 1)), axis = 0)