from rotation import Rotation
from numerical import Constants
from rotmat3D import RotMat3D
from rotseq import RotSeq
from frame import Frame


r = RotMat3D()
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

f = Frame()
print f.base, f.z



