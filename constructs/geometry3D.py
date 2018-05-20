import numpy as np 

from rigidbody import RigidBody
from base import Frame, Vector, Axis
from .. numeric.constants import Constants 
from .. numeric.operations import Operations 


#TODO: Add local frame computation for all geometric objects
#TODO: Add computation of inertia tensors and shift theorem

class Cube(RigidBody):

    def __init__(self, mass=1.0, size=1.0, com=Vector()):

        super(Cube, self).__init__(mass, com)
        
        self.size = size 
        self.base_frame = self.com.base_frame 

        self.render_object = RenderObjects.cube

    def compute_surface_area(self):

        return 6*(self.size**2)

    def compute_volume(self):

        return self.size**3

    def compute_density(self):

        return self.mass/self.compute_volume()

class Cuboid(RigidBody):

    def __init__(self, mass=1.0, size_x=1.0, size_y=1.0, size_z=1.0, com=Vector()):

        super(Cuboid, self).__init__(mass, com)

        self.size_x = size_x 
        self.size_y = size_y 
        self.size_z = size_z 
        self.base_frame = self.com.base_frame

        self.render_object = RenderObjects.cuboid

    def compute_surface_area(self):

        return 2*(self.size_x*self.size_y + self.size_y*self.size_z + self.size_z*self.size_x)

    def compute_volume(self):

        return self.size_x*self.size_y*self.size_z

    def compute_density(self):

        return self.mass/self.compute_volume()

class Sphere(RigidBody):

    def __init__(self, mass=1.0, radius = 1.0, com = Vector()):

        super(Sphere, self).__init__(mass, com)
        self.radius = radius 
        self.base_frame = self.com.base_frame

        self.render_object = RenderObjects.sphere

    def compute_surface_area(self):

        return 4*Constants.pi*(self.radius**2)

    def compute_volume(self):

        return (4.0/3.0)*Constants.pi*(self.radius**3)

    def compute_density(self):

        return self.mass/self.compute_volume()


class Cylinder(RigidBody):

    def __init__(self, mass=1.0, radius = 1.0, height = 1.0, com = Vector()):

        super(Cylinder, self).__init__(mass, com)
        self.radius = radius 
        self.height = height 
        self.base_frame = self.com.base_frame

        self.render_object = RenderObjects.cylinder

    def compute_surface_area(self):

        return 2*Constants.pi*self.radius*self.height

    def compute_volume(self):

        return Constants.pi*(self.radius**2)*self.height

    def compute_density(self):

        return self.mass/self.compute_volume()













