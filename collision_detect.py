"""COLLISION DETECTION FUNCTION"""
from constants import BLOCK_SIZE, LIMIT_X_Y, SOFT_HIT_COLOR, SNAKE_HT_COLOR, SNAKE_HEAD_COLOR


def is_collided(snake, food):
    snake.head.color(SNAKE_HEAD_COLOR)
    if snake.head.distance(food.position()) < BLOCK_SIZE:
        snake.head.color(SOFT_HIT_COLOR)
        return True
    return False


def is_collided_with_wall(snake):
    """check collision between snake head and wall"""
    hit_left_or_right = snake.head.xcor() < -LIMIT_X_Y or snake.head.xcor() > LIMIT_X_Y
    hit_up_or_down = snake.head.ycor() < -LIMIT_X_Y or snake.head.ycor() > LIMIT_X_Y

    if hit_left_or_right or hit_up_or_down:
        snake.head.color(SNAKE_HT_COLOR)
        snake.draw_boundaries(SOFT_HIT_COLOR)
        return True
    # no collision found
    return False


def is_collided_with_tail(snake):
    """check collision with tail"""
    # seg[0] is head seg[1] is neck. seg[2] and seg[3] is impossible to catch itself
    # So, start from seg[4].
    if snake.len > 4:
        for i in range(4, snake.len):
            if snake.head.distance(snake.segments[i].position()) < BLOCK_SIZE:
                snake.segments[i].color(SNAKE_HT_COLOR)
                return True
    return False
