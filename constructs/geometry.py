import numpy as np 

from base import Frame, Vector, Axis
from .. numeric.constants import Constants 
from .. numeric.operations import Operations 


#TODO: Add local frame computation for all geometric objects

class Cube(object):

    def __init__(self, units = Constants.m, size = 1.0, center = Vector()):

        self.units = units 
        self.size = size 
        self.center = center 
        self.base_frame = center.base_frame 
        self.mass = 1

    def compute_surface_area(self):

        return 6*(self.size**2)

    def compute_volume(self):

        return self.size**3

    def compute_density(self):

        return self.mass/self.compute_volume

class Cuboid(object):

    def __init__(self, units = Constants.m, size_x = 1.0, size_y = 1.0, size_z =1.0, center = Vector()):

        self.units = units 
        self.size_x = size_x 
        self.size_y = size_y 
        self.size_z = size_z 
        self.center = center 
        self.base_frame = center.base_frame
        self.mass = 1.0

    def compute_surface_area(self):

        return 2*(self.size_x*self.size_y + self.size_y*self.size_z + self.size_z*self.size_x)

    def compute_volume(self):

        return self.size_x*self.size_y*self.size_z

    def compute_density(self):

        return self.mass/self.compute_volume

class Sphere(object):

    def __init__(self, units = Constants.m, radius = 1.0, center = Vector()):

        self.units = units 
        self.radius = radius 
        self.center = center
        self.base_frame = center.
        self.mass = 1.0

    def compute_surface_area(self):

        return 4*Constants.pi*(self.radius**2)

    def compute_volume(self):

        return (4.0/3.0)*Constants.pi*(self.radius**3)

    def compute_density(self):

        return self.mass/self.compute_volume


class Cylinder(object):

    def __init__(self, units = Constants.m, radius = 1.0, height = 1.0, center = Vector()):

        self.units = units 
        self.radius = radius 
        self.height = height 
        self.center = center 
        self.base_frame = center.base_frame
        self.mass = 1.0

    def compute_surface_area(self):

        return 2*Constants.pi*self.radius*self.height

    def compute_volume(self):

        return Constants.pi*(self.radius**2)*self.height

    def compute_density(self):

        return self.mass/self.compute_volume













