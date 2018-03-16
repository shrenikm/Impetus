import numpy as np

from transformation import Transformation
from .. numeric.constants import Constants
from .. numeric.operations import Operations
from .. constructs.base import Frame

# Class that implements operations related to rotation matrices.


class TfMat(Transformation, Operations):

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

    def gen_tm_from_rot(self, rm, d=Constants.vector_zero):

        t = np.concatenate((np.concatenate((rm, d), axis=1),
                            Constants.vector_zero_hom.T), axis=0)

        return t

    def gen_tm_single_frame(self, frame):

        r = np.zeros([3, 3])
        r[0, :] = frame.x.T
        r[1, :] = frame.y.T
        r[2, :] = frame.z.T

        return self.gen_tm_from_rot(r, frame.origin)

    def gen_tm_all_frame(self, frame):

        r = self.gen_rm_single_frame(frame)
        frame_tmp = frame

        while frame_tmp.base is not None:

            r = np.dot(self.gen_rm_single_frame(frame_tmp.base), r)
            frame_tmp = frame_tmp.base

        return self.gen_tm_from_rot(r, frame.compute_world_origin())

    def gen_tm_rotframe(self, frame_start, frame_end):

        r_start = self.gen_rm_all_frame(frame_start)
        r_end = self.gen_rm_all_frame(frame_end)
        r = np.dot(r_start.T, r_end)

        return self.gen_tm_from_rot(r, frame_end.compute_world_origin() - frame_start.compute_world_origin())