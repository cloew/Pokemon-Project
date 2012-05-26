import commands
import pygame
from pygame.locals import *

keyBindings = {K_UP:commands.UP,
                       K_w:commands.UP,
                       K_DOWN:commands.DOWN,
                       K_s:commands.DOWN,
                       K_LEFT:commands.LEFT,
                       K_a:commands.LEFT,
                       K_RIGHT:commands.RIGHT,
                       K_d:commands.RIGHT,
                       K_ESCAPE:commands.EXIT,
                       K_ENTER:commands.SELECT}