"""
Creating a 3D histogram in the RGB colorspace

"""

# import the necessary packages
import cv2

class RGBHistogram:
	def __init__(self, bins):
		# store the number of bins the histogram will use
		self.bins = bins

	def describe(self, image):
		# compute a 3D histogram in the RGB colorspace
		hist = cv2.calcHist([image], [0, 1, 2], None, self.bins, [0, 256, 0, 256, 0, 256])
         # normalize the histogram so that images scaled larger or smaller will have the same histogram
		hist = cv2.normalize(hist)
		# return out 3D histogram array
		return hist.flatten()