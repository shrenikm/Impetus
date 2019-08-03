import numpy as np 
import math

from Impetus.constructs.base import Frame, Vector, Axis
from Impetus.constructs.rigidbody import RigidBody
from Impetus.numeric.constants import Physical, Units, Struct, Matrices, Colors, RenderObjects
from Impetus.numeric.operations import Operations 


#TODO: Add local frame computation for all geometric objects
#TODO: Add computation of inertia tensors and shift theorem

class Line(RigidBody):

    def __init__(self, mass=1.0, length=1.0, com=Vector()):

        super(Line, self).__init__(mass, com)
        self.length = length
        self.base_frame = self.com.base_frame

        self.render_object = RenderObjects.line
        self.color = Colors.brown


    def compute_density(self):

        return self.mass/self.length












