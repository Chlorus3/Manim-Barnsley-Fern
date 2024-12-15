from manim import *
from random import choices

NUMBER_OF_POINTS = 20000 # reduce this if it takes too long to render

def fern(scale, y_shift):
	"""Usage: create an object such as 'f = fern()' then use the next(f) to get the next value

	Args:
		scale (_type_): how x and y should be scaled for display
		y_shift (_type_): useful for moving up and down the image

	Yields:
		_type_: x,y coordinates
	"""
	x, y = 0, 0

	options = [0, 1, 2, 3]
	weights = [0.01, 0.85, 0.07, 0.07]

	while True:
		c = choices(options, weights)[0]

		if c == 0:
			x, y = 0, 0.16 * y
		elif c == 1:
			x, y = (0.85 * x) + (0.04 * y), (-0.04 * x) + (0.85 * y) + 1.6
		elif c == 2:
			x, y = (0.2 * x) - (0.26 * y), (0.23 * x) + (0.22 * y) + 1.6
		elif c == 3:
			x, y = (-0.15 * x) + (0.28 * y), (0.26 * x) + (0.24 * y) + 0.44

		yield (x * scale), (y * scale) + y_shift


class BarnsleyFern(Scene):
	def construct(self):
		# change this to how you want, this has been set to fill the screen by default, 
		#  if you reduce the number of points reduce the scale as well so it is not as noticable
		fern_point = fern(scale=0.75, y_shift=-3.8)
		points = VGroup()

		for _ in range(NUMBER_OF_POINTS):
			x, y = next(fern_point)
			points.add(
				Dot([x, y, 0],
					radius=0.01,
					color=GREEN
				)
			)

		self.add(points)