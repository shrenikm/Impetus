import numpy as np 
import math

from rigidbody import RigidBody
from base import Frame, Vector, Axis
from .. numeric.constants import Physical, Units, Struct, Matrices, Colors, RenderObjects
from .. numeric.operations import Operations 


#TODO: Add local frame computation for all geometric objects
#TODO: Add computation of inertia tensors and shift theorem

class Disc(RigidBody):

    def __init__(self, mass=1.0, radius=1.0, com=Vector()):

        super(Disc, self).__init__(mass, com)
        self.radius = radius
        self.base_frame = self.com.base_frame

        self.render_object = RenderObjects.disc
        self.color = Colors.brown

    def compute_surface_area(self):

        return 2*math.pi*self.radius

    def compute_density(self):

        return self.mass/self.compute_area()












