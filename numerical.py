import numpy as np 
import math

class Constants(object):

	pi = np.pi
	e = np.e

	def __init__(self):
		pass

class Operations(Constants):

	def __init__(self):
		pass

	@classmethod
	def rad2deg(cls, angle):
		return math.degrees(angle)

	@classmethod
	def deg2rad(cls, angle):
		return math.radians(angle)




