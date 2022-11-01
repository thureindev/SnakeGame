"""Snake class"""
from turtle import Turtle as Segment
from constants import BLOCK_SIZE, LIMIT_X_Y,\
    BOUNDARY_X_Y, BOUNDARY_COLOR,\
    SNAKE_SHAPE, SNAKE_HEAD_COLOR, SNAKE_BODY_COLOR

UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0


class Snake:
    def __init__(self):
        self.block_size = BLOCK_SIZE
        self.limit_x_y = LIMIT_X_Y

        self.wall_boundaries = Segment()
        self.draw_boundaries(BOUNDARY_COLOR)

        self.segments = []
        self.len = 0

        self.setup_snake()
        self.head = self.segments[0]
        self.neck = self.segments[1]

    def setup_snake(self, seg_count=3, head_color=SNAKE_HEAD_COLOR):
        """setup snake at game start"""
        # create segments of a snake body, and position at the center
        pos_x = 0
        for i in range(seg_count):
            self.make_new_segment(pos_x, 0)
            pos_x -= self.block_size

        # set snake head  color and heading
        self.segments[0].color(head_color)
        self.segments[0].setheading(RIGHT)

    def draw_boundaries(self, color):
        self.wall_boundaries.clear()

        self.wall_boundaries.hideturtle()
        self.wall_boundaries.color(color)
        self.wall_boundaries.pensize(5)

        self.wall_boundaries.penup()
        self.wall_boundaries.setpos(-BOUNDARY_X_Y, BOUNDARY_X_Y)
        self.wall_boundaries.pendown()
        self.wall_boundaries.goto(BOUNDARY_X_Y, BOUNDARY_X_Y)
        self.wall_boundaries.goto(BOUNDARY_X_Y, -BOUNDARY_X_Y)
        self.wall_boundaries.goto(-BOUNDARY_X_Y, -BOUNDARY_X_Y)
        self.wall_boundaries.goto(-BOUNDARY_X_Y, BOUNDARY_X_Y)

    def make_new_segment(self, pos_x, pos_y, color=SNAKE_BODY_COLOR, shape=SNAKE_SHAPE):
        """make a new segment and append it to snake segments list"""
        new_segment = Segment()
        new_segment.color(color)
        new_segment.shape(shape)
        new_segment.penup()
        new_segment.setposition(pos_x, pos_y)

        self.segments.append(new_segment)
        self.len += 1

    def grow(self):
        pos_x = self.segments[self.len - 1].xcor()
        pos_y = self.segments[self.len - 1].ycor()
        self.make_new_segment(pos_x, pos_y)

    def move(self):
        # body moves first
        for i in range(self.len - 1, 0, -1):
            self.segments[i].setpos(self.segments[i - 1].pos())
        self.neck.setheading(self.head.heading())
        self.head.forward(self.block_size)
    """using segment[1] as neck is necessary because - 
the user can trick the input by pressing keys quickly

example case - 
head is directed in dir RIGHT 
user quickly press down + left keys; head dir is changed to down which is valid, then immediately changed to left
then head direction is changed to dir LEFT which is what we want to prevent

therefore I used neck_dir (segment[1].heading) instead of head_dir (segment[0].heading)
    """

    def dir_up(self):
        if self.neck.heading() != DOWN:
            self.head.setheading(UP)

    def dir_down(self):
        if self.neck.heading() != UP:
            self.head.setheading(DOWN)

    def dir_left(self):
        if self.neck.heading() != RIGHT:
            self.head.setheading(LEFT)

    def dir_right(self):
        if self.neck.heading() != LEFT:
            self.head.setheading(RIGHT)

    def reset(self):
        self.segments.clear()
        self.len = 0
        self.setup_snake()