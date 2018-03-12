import engine.game as game
import engine.primitives as primitives
from engine.physics import Vec2
from engine.entity import Entity


class Grid(Entity):
	def __init__(self):
		super().__init__()

	def generate_ii(self):
		return game.get_low_ii()

	def render(self):
		zoom = game.camera.zoom
		if zoom >= 0.05:
			return
		color = 4*(1 - (zoom/0.05)**0.5,)
		a, b, c, d = map(int, game.camera.rect())
		'''	a      b
			|      |
		c --+------+--
			|      |
		d --+------+--
			|      |  '''

		# horizontal
		for x in range(a - 1, b + 2):
			primitives.line((x, c - 1), (x, d + 1),
				color=color, stroke=0)

		#vertical
		for y in range(c - 1, d + 2):
			primitives.line((a - 1, y), (b + 1, y),
				color=color, stroke=0)

