from abc import ABCMeta, abstractmethod

import numpy as np
import math

from Impetus.numeric.constants import Physical, Units, Struct, Matrices, RenderObjects
from Impetus.numeric.operations import Operations
from Impetus.constructs.base import Configuration


# Blueprint for the RRT construct


class RRT(object):

    __metaclass__ = ABCMeta

    def __init__(self, config):

        self.config = config

    def set_config(self, config):

        self.config = config

    @abstractmethod
    def initialize_random_configuration(self):

        pass

    @abstractmethod
    def compute_distance(self, x, y):

        pass

    @abstractmethod
    def is_config_in_free(self, x):

        pass

    @abstractmethod
    def is_line_in_free(self, x, y):

        pass
