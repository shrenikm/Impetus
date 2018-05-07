from abc import ABCMeta, abstractmethod

import numpy as np
from math import sin
from math import cos
from math import pi


from .. numeric.constants import Constants
from .. numeric.operations import Operations


# Main class that serves as a blueprint for all rotation related functions.
# Serves as a blueprint for future transformation tasks that need to be implemented by all sub classes


class Transformation(object):

    __metaclass__ = ABCMeta

    def __init__(self):
        pass


