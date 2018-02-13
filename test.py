import numpy as np

from rotation import Rotation
from numerical import Constants
from rotmat import RotMat
from rotseq import RotSeq
from frame import Frame


r = RotMat()
print r.get_units()
r.set_units('deg')
print r.get_units()

# print RotMat3D.pi, r.pi, RotMat3D.e
# print RotMat3D.rad2deg(RotMat3D.pi)
# print RotMat3D.deg2rad(180)
# print r.gen_rmx(30)
# print r.gen_rmy(30)
# print r.gen_rmz(30)

seq = RotSeq('deg')
seq.add_rotation([30, 30, 20], [Constants.gx, Constants.lz, Constants.ly])
seq.add_rotation([90], [Constants.lx])
print seq.sequence

f2 = Frame(x=np.random.rand(3, 1),
           y=np.random.rand(3, 1), z=np.random.rand(3, 1))
f3 = Frame(base=f2, x=np.random.rand(3, 1),
           y=np.random.rand(3, 1), z=np.random.rand(3, 1))
f4 = Frame(base=f3, x=np.random.rand(3, 1),
           y=np.random.rand(3, 1), z=np.random.rand(3, 1))
print r.gen_rm_rotframe(f4)
# print f.base, f.z
