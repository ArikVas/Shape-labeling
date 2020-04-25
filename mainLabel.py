import numpy as np
import tensorflow as tf
from matplotlib import pyplot as plt
import math
from tensorflow import keras
NMag = 0.01
lineEq = lambda a,b,x:  a*x + b
linesNum = 10000
PointsOnLine = 1000
noise = (0.5 - np.random.rand(PointsOnLine, linesNum)) * NMag
xLine = np.random.rand(PointsOnLine, linesNum)
a = np.random.rand(linesNum)
b = np.random.rand(linesNum)
a = np.tile(a,(PointsOnLine,1))#np.repeat(a, PointsOnLine,axis=1)#.reshape(PointsOnLine, linesNum)
b = np.tile(b,(PointsOnLine,1))#.reshape(PointsOnLine, linesNum)
yLine = lineEq(a,b,xLine) + noise

CircleNum = 10000
pointsOnCircle = 1000
noiseX = (0.5 - np.random.rand(pointsOnCircle, CircleNum)) * NMag
noiseY = (0.5 - np.random.rand(pointsOnCircle, CircleNum)) * NMag
rad = np.random.rand(CircleNum)
x0 = np.random.rand(CircleNum)
y0 = np.random.rand(CircleNum)
rad = np.tile(rad,(pointsOnCircle,1))#repeat(rad, pointsOnCircle, axis=1).reshape(pointsOnCircle, linesNum)
x0 = np.tile(x0, (pointsOnCircle,1))#.reshape(pointsOnCircle, linesNum)
y0 = np.tile(y0, (pointsOnCircle,1))#.reshape(pointsOnCircle, linesNum)
CircleAngle = np.random.rand(pointsOnCircle, CircleNum) * np.pi * 2
xC = np.cos(CircleAngle) * rad + x0 + noiseX
yC = np.sin(CircleAngle) * rad + y0 + noiseY

#plot samples
plt.figure()
plt.plot(xC[:,0:3], yC[:,0:3],'.')
plt.title('circles')

plt.figure()
plt. plot(xLine[:,0:3], yLine[:,0:3],'.')
plt.title('lines')

plt.show(block=True)
############################
