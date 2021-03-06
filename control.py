import engine.game as game
from engine.physics import Vec2
from engine.event import Event
from bullet import Bullet
import bullet
from bubble import Bubble, Structure
from pyglet.window import mouse
from pyglet.window import key
import loader

import json

#key.symbol_string(key.O)
'''NOTHING = Structure([])
BUBBLE = [Structure([Bubble((0, 0), i)]) for i in range(5)]
NEG = Structure(loader.load('doubleneg.txt')[0])
OR = Structure(loader.load('doubleor.txt')[0])
DIODE = Structure(loader.load('diode.txt')[0])
AND = Structure(loader.load('doubleand.txt')[0])
XOR = Structure(loader.load('xor.txt')[0])
ADD = Structure(loader.load('add.txt')[0])
BOMB = Structure(loader.load('bomb.txt')[0])'''

with open('structs.json') as file:
	structs_path = json.load(file)

structs = dict()
for k, path in structs_path.items():
	structs[k] = Structure(loader.load(path)[0])

'''structs = {
	key.SEMICOLON: NOTHING,
	key._1: BUBBLE[1],
	key._2: BUBBLE[2],
	key._3: BUBBLE[3],
	key._4: BUBBLE[4],
	key.N: NEG,
	key.O: OR,
	key.K: DIODE,
	key.J: AND,
	key.X: XOR,
	key.L: ADD,
	key.B: BOMB,
	key.F: Structure(loader.load('decoder.txt')[0]),
	key._8: Structure(loader.load('osm.txt')[0]),
	key._6: Structure(loader.load('sest.txt')[0]),
	key.M: Structure(loader.load('memory.txt')[0]),
	key.R: Structure(loader.load('rett.txt')[0]),
}'''


structs_path = dict()





struct = Structure([])
struct.add()

filename = None


def change_struct(new):
	global struct
	struct.remove()
	struct = new
	struct.add()

def init():
	@game.window.event
	def on_mouse_press(mx, my, button, modifiers):
		x, y = game.camera.click_transform(Vec2(mx, my))
		x, y = x + 0.5, y + 0.5
		x = int(x) - (1 if x < 0 else 0)
		y = int(y) - (1 if y < 0 else 0)
		if button == mouse.LEFT:
			'''try:
				l = game.bubbles[x, y].lives
				l += 1
				if l == 5:
					l = 1
				game.bubbles[x, y].lives = l
			except KeyError:
				struct.realize((x, y))'''
			struct.realize((x, y))

		elif button == mouse.RIGHT:
			try:
				game.bubbles[x, y].remove()
			except KeyError:
				pass
		elif button == mouse.MIDDLE:
			try:
				game.bubbles[x, y].explode()
			except KeyError:
				pass


	@game.window.event
	def on_key_press(symbol, modifiers):
		global filename
		
		ss = key.symbol_string(symbol)
		
		if   symbol == key.F1:
			loader.clear()
			filename = None
		elif symbol == key.F2:
			filename = input('filename:')
			loader.clear()
			arr, width, height = loader.load(filename)
			game.camera.x = width/2
			game.camera.y = height/2
			for b in arr:
				b.add()

		elif symbol == key.F5:
			loader.clear()
			if(filename):
				arr, width, height = loader.load(filename)
				game.camera.x = width/2
				game.camera.y = height/2
				for b in arr:
					b.add()
		elif symbol == key.S:
			if modifiers & key.MOD_CTRL:
				if filename:
					loader.save(filename)
				else:
					filename = input('filename:')
					loader.save(filename)

		elif symbol in structs.keys():
			change_struct(structs[symbol])

		elif symbol == key.Q:
			bullet.speed_cons *=0.8
		elif symbol == key.E:
			bullet.speed_cons *= 1.25

		elif modifiers & key.MOD_CTRL and symbol != 65507:
			name = 'key-{}.txt'.format(ss)
			loader.save(name)
			structs[symbol] = loader.load(name)[0]
			structs_path[ss] = name
			with open('structs.json', 'w') as file:
				json.dump(structs_path, file, indent=4, separators=(',', ': '))

		elif ss in structs.keys():
			change_struct(structs[ss])





	@game.window.event
	def on_key_release(symbol, modifiers):
		pass

def add():
	Event(init).add()