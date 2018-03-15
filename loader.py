from bubble import Bubble
from bullet import Bullet
import engine.game as game

def load(filename):
	arr = []
	print('load', filename)
	try:
		with open('saves/' + filename, 'r') as file:
			columns = list(reversed(list(file)))
	except FileNotFoundError:
		print(filename, 'not found')
		return ([], 0, 0)

	for y, line in enumerate(columns):
		for x, char in enumerate(line.rstrip()):
			if char != ' ':
				arr.append(Bubble((x, y), int(char)))

	height = len(columns)
	width = max(map(len, columns), default=1) - 1 #for \n

	return (arr, width, height)

def clear():
	print('clear')
	for entity in game.entities.values():
		if entity.__class__ in (Bubble, Bullet):
			entity.remove()

def save(filename):
	print('save', filename)
	bubbles = game.bubbles.values()
	get_x = lambda e: e.pos[0]
	x_min = min(map(get_x, bubbles), default=0)
	x_max = max(map(get_x, bubbles), default=0)
	get_y = lambda e: e.pos[1]
	y_min = min(map(get_y, bubbles), default=0)
	y_max = max(map(get_y, bubbles), default=0)

	with open('saves/' + filename, 'w') as file:
		for y in range(y_max, y_min - 1, -1):
			for x in range(x_min, x_max + 1):
				try:
					char = str(game.bubbles[x, y].lives)
				except KeyError:
					char = ' '
				file.write(char)
			if y != y_min:
				file.write('\n')