import engine.game as game
import engine.primitives as primitives
from engine.physics import Vec2
from engine.entity import Entity


class Bullet(Entity):
	def __init__(self, pos, speed=Vec2(0, 0)):
		super().__init__()
		self.pos = pos
		self.speed = speed

	def generate_ii(self):
		return game.get_high_ii()

	def update(self, dt):
		self.pos += dt*self.speed
		if self.pos.length > 10000:
			self.remove()

		x, y = self.pos + Vec2(0.5, 0.5)
		x = int(x) - (1 if x < 0 else 0)
		y = int(y) - (1 if y < 0 else 0)
		try:
			bubble = game.bubbles[x, y]
			if bubble.damage():
				self.remove()
		except KeyError:
			pass



	def render(self):
		primitives.circle(self.pos, 0.25, color=4*(1,))
