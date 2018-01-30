import numpy as np 

from rotation import Rotation

from numerical import Constants
from numerical import Operations

class RotMat(Rotation, Operations):

	def __init__(self, units = 'rad'):
		super(RotMat, self).__init__(units)
		
	def get_units(self):
		return super(RotMat, self).get_units()

	def set_units(self, units):
		super(RotMat, self).set_units(units)

