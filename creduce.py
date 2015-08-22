import sys
import numpy as np
import cv2

def colorReduce(img, div=64):
  nRows = img.shape[0]
  nCols = img.shape[1]
  nChannels = img.shape[2]
  total = nRows*nCols*nChannels
  print "%d rows %d cols %d channels" % (nRows, nCols, nChannels)
  progress = 0

  for j in range(0,nRows-1):
    for i in range(0, nCols-1):
      for c in range(0, nChannels -1):
        img[j][i][c] = img[j][i][c] / div * div + div / 2
        progress = progress + 1
        print "Progress is %d of %d" % (progress, total)

if len(sys.argv) < 2:
  print "Missing required filename argument."
  sys.exit(1)

filename = sys.argv[1]

div = 64

if len(sys.argv) == 3:
  div = int(sys.argv[2])

srcBGR = cv2.imread(filename)
if srcBGR == None:
  print "Could not open file " + filename
  sys.exit(1)

colorReduce(srcBGR, div)
reducedName = "reduced-{}-{}".format(div, filename)
cv2.imwrite(reducedName, srcBGR)
print "Done reducing"

