from rotation import Rotation
from rotmat import RotMat

r = RotMat()
print r.get_units()
r.set_units('deg')
print r.get_units()

print RotMat.pi, r.pi, RotMat.e
print RotMat.rad2deg(RotMat.pi)
print RotMat.deg2rad(180)

