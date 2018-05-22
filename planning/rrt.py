import numpy as np
import math
import random

from .. numeric.constants import Physical, Units, Struct, Matrices, RenderObjects
from .. numeric.operations import Operations
from .. constructs.base import Configuration
from .. planning.base import RRT

# Standard RRT implementations


class rrt_standard(RRT):

    def __init__(self, config=Configuration()):

        super(rrt_standard, self).__init__(config)

    def initialize_random_configuration(self):

        rand_base = np.random.rand(self.config.dim, 1)
        a = self.config.get_lower_limits_arr()
        b = self.config.get_upper_limits_arr()
        c = a + rand_base*(b-a)

        cf = Configuration()
        cf.dim = self.config.dim
        cf.value = c
        cf.set_lower_limits = self.config.lower_limits
        cf.set_upper_limits = self.config.upper_limits

        return cf

    def initialize_random_configuration_in_free(self):

        cf = self.initialize_random_configuration()
        while(not is_config_in_free(cf)):
            cf = self.initialize_random_configuration()

        return cf

    def compute_distance(self, xc, yc):

        return np.linalg.norm(xc.value - yc.value)

    def is_config_in_free(self, xc):

        pass

    def is_line_in_free(self, xc, yc):

        flag = True
        multiplier = 100
        for i in range(multiplier*int(self.compute_distance(xc, yc))):
            if(not is_config_in_free(xc.value + (i/(multiplier*int(self.compute_distance(xc, yc))))*(yc_value - xc_value))):
                flag = False

        return flag


