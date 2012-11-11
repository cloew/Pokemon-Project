import commands

from kao_console.ascii import *

keyBindings = {KAO_UP:commands.UP,
                       ord("w"):commands.UP,
                       ord("W"):commands.UP,
                       KAO_DOWN:commands.DOWN,
                       ord("s"):commands.DOWN,
                       ord("S"):commands.DOWN,
                       KAO_LEFT:commands.LEFT,
                       ord("a"):commands.LEFT,
                       ord("A"):commands.LEFT,
                       KAO_RIGHT:commands.RIGHT,
                       ord("d"):commands.RIGHT,
                       ord("D"):commands.RIGHT,
                       ESCAPE:commands.EXIT,
                       ENDL:commands.SELECT}