from __future__ import print_function

import numpy as np 

from Impetus.constructs.base import Vector

#Rigid body class that is that parent class of all other 3d geometric objects


class RigidBody(object):

    def __init__(self, mass = 1.0, com = Vector()):

        self.mass = mass 
        self.com = com

        
