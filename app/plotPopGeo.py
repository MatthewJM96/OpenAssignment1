import utils

import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

import sys

# Read chosen data file and if reading fails, render error.
fileData = utils.readFile("data/" + sys.argv[1])

# Transpose file data.
fileDataTransposedTemp = np.transpose(fileData)
fileDataTransposed = []
fileDataTransposed.append(fileDataTransposedTemp[0])
fileDataTransposed.append(fileDataTransposedTemp[1])

# Convert file data to correct types.
temp1 = []
for entry in fileDataTransposedTemp[2]:
  temp1.append(int(entry))
fileDataTransposed.append(temp1)
temp2 = []
for entry in fileDataTransposedTemp[3]:
  temp2.append(float(entry))
fileDataTransposed.append(temp2)
temp3 = []
for entry in fileDataTransposedTemp[4]:
  temp3.append(float(entry))
fileDataTransposed.append(temp3)

#ukBackgroundImage = mpimg.imread("app/static/Uk_outline_map.png")

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

for i, entry in enumerate(fileDataTransposed[0]):
  x = fileDataTransposed[4][i]
  y = fileDataTransposed[3][i]
  z = fileDataTransposed[2][i]
  if (fileDataTransposed[1][i].lower() == "city"):
    c = 'r'
    m = 'o'
  else:
    c = 'b'
    m = '^'
  ax.scatter(x, y, z, c=c, marker=m)
  
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')
ax.set_zlabel('Population')

plt.show()