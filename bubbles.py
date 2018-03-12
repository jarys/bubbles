import engine.game as game
game.init()

#import rule_connect
#rule_connect.add()
from engine.camera import Camera
Camera(zoom=0.02).add()

import engine.assets.camera_control as camera_control
camera_control.add()

from bullet import Bullet
from bubble import Bubble
import random
from engine.physics import Vec2
#Bubble((0, 0), 1).add()

import control
control.add()

from grid import Grid
Grid().add()

game.start()