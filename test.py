import numpy
from numpy import  *
randMat = mat(random.rand(4,4))
print(randMat)
invRandmat = randMat.I
print(invRandmat)
multMat = invRandmat * randMat
print(multMat)
myEye = multMat - eye(4)
print(myEye)
print(eye(4))
