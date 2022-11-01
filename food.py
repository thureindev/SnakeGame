"""Food class"""
import random
from turtle import Turtle as T
from constants import BLOCK_SIZE, LIMIT_X_Y, FOOD_COLOR, FOOD_SIZE, FOOD_SHAPE


class Food(T):
    def __init__(self):
        super().__init__()
        self.setup_food()
        self.set_random_pos()

    def setup_food(self, color=FOOD_COLOR, shape=FOOD_SHAPE, size=FOOD_SIZE):
        self.color(color)
        self.shape(shape)
        self.shapesize(size)
        self.penup()

    def set_random_pos(self):
        # generate random coordinates
        pos_x = random.randint(-LIMIT_X_Y, LIMIT_X_Y)
        pos_y = random.randint(-LIMIT_X_Y, LIMIT_X_Y)

        # snap random coordinates to BLOCKSIZE
        mod_x = pos_x % BLOCK_SIZE
        mod_y = pos_y % BLOCK_SIZE
        if mod_x != 0:
            pos_x += (BLOCK_SIZE - mod_x)
        if mod_y != 0:
            pos_y += (BLOCK_SIZE - mod_y)

        #TODO   # AVOID using random coordinates spawning at the points where snake body already has taken place

        # finally set position
        self.setposition(pos_x, pos_y)
