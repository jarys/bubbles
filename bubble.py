import engine.game as game
import engine.primitives as primitives
from engine.physics import Vec2
from engine.entity import Entity
from bullet import Bullet
from pyglet.gl import glTranslatef

game.bubbles = dict()
colors = [
	(0.7, 0.7, 0.7, 1),
	(1, 0, 0, 1), #1 red
	(0.7, 0.5, 0, 1), #2 yellow
	(0, 1, 0, 1), #3 green
	(0.3, 0.3, 1, 1) #4 blue
]
es = 12 #explosion speed
class Bubble(Entity):
	def __init__(self, pos, lives=1):
		super().__init__()
		self.pos = pos
		self.lives = lives

	def damage(self):
		if self.lives:
			self.lives -= 1
			if self.lives <= 0:
				self.explode()
			return True
		else:
			return False

	def explode(self):
		self.remove()
		for v in ((0, es), (es, 0), (0, -es), (-es, 0)):
			Bullet(Vec2(*self.pos), Vec2(*v)).add()

	def render(self):
		primitives.circle(self.pos, 0.4*1.1**(-self.lives),
			color=colors[self.lives])

	def init(self):
		game.bubbles[self.pos] = self

	def outit(self):
		del game.bubbles[self.pos]
		#remove from group

mouse = Vec2(0, 0)

class Structure(Entity):
	def __init__(self, data):
		super().__init__()
		self.data = data

	def realize(self, pos):
		x0, y0 = pos
		for bubble in self.data:
			x = x0 + bubble.pos[0]
			y = y0 + bubble.pos[1]
			try:
				game.bubbles[x, y].remove()
			except KeyError:
				pass
			Bubble((x, y), bubble.lives).add()

	def render(self):
		glTranslatef(mouse[0], mouse[1], 0)

		for bubble in self.data:
			bubble.render()

		glTranslatef(-mouse[0], -mouse[1], 0)

	def init(self):
		@game.window.event
		def on_mouse_motion(x, y, dx, dy):
			global mouse
			mouse = game.camera.click_transform(Vec2(x, y)) 