from abc import ABCMeta, abstractmethod

import numpy as np 
from math import sin 
from math import cos
from math import pi

class Rotation(object):

	__metaclass__ = ABCMeta

	def __init__(self, units = 'rad'):
		self.units = units

	@abstractmethod
	def get_units(self):
		return self.units 

	@abstractmethod
	def set_units(self, units):
		self.units = units

	# def compute_axis_rm(self, angle, axis):

	# 	if self.units = 'deg':
	# 		angle = angle * pi / 180.0

	# 	r = np.zeros([3, 3])
	# 	if axis == 'x':
	# 		r[0, 0] = 1
	# 		r[1, 1] = cos(angle)




