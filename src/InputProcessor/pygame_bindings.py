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
               K_RETURN:commands.SELECT}
               
keyStrings = {K_UP:"UP ARROW",
              K_w:"w",
              K_DOWN:"DOWN ARROW",
              K_s:"s",
              K_LEFT:"LEFT ARROW",
              K_a:"a",
              K_RIGHT:"RIGHT ARROW",
              K_d:"d",
              K_ESCAPE:"ESCAPE",
              K_RETURN:"ENTER"}