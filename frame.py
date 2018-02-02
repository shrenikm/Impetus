import numpy as np 

from numerical import Constants

# Class that deals with creating reference frames.
# Whenever dealing with frames, the standard frame must be created first with an empty dictionary base.

class Frame(Constants):


    def __init__(
            self, base = {}, 
            x = Constants.std_axis_x, 
            y = Constants.std_axis_y,
            z = Constants.std_axis_z, 
            is_std = True):

        self.base = base
        self.x = x
        self.y = y 
        self.z = z 
        self.is_std = is_std





