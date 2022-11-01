import turtle
from turtle import Screen
import snake as sk
import food as f
import scoreboard as sc
import collision_detect as c
from constants import CLOCK_TICK, BLOCK_SIZE, LENGTH_X_Y, LIMIT_X_Y
import time

SCREEN = Screen()

# start with true so the new game can be reset
is_gameover = True
is_paused = False

foo = False


def game():
    # update gameover status
    global is_gameover
    is_gameover = False
    global is_paused

    # setup game objects
    snake = sk.Snake()
    food = f.Food()
    score = sc.Scoreboard()

    # setup player controls
    SCREEN.listen()
    SCREEN.onkeypress(key="Up", fun=snake.dir_up)
    SCREEN.onkeypress(key="Left", fun=snake.dir_left)
    SCREEN.onkeypress(key="Down", fun=snake.dir_down)
    SCREEN.onkeypress(key="Right", fun=snake.dir_right)
    SCREEN.onkeypress(key="w", fun=snake.dir_up)
    SCREEN.onkeypress(key="a", fun=snake.dir_left)
    SCREEN.onkeypress(key="s", fun=snake.dir_down)
    SCREEN.onkeypress(key="d", fun=snake.dir_right)
    #   #   restart_game only works when is_gameover == True
    SCREEN.onkeypress(key="space", fun=check_gameover_and_pause)
    SCREEN.onkeypress(key="p", fun=check_gameover_and_pause)

    # start scoreboard display
    score.update_scoreboard()
    while not is_gameover:
        # to pause the game
        if not is_paused:
            # # # GAME LOGIC STARTS HERE ----- -----
            # # # ----- ----- ----- ----- ----- -----
            score.update_scoreboard()

            snake.move()
            # food check
            if c.is_collided(snake, food):
                snake.grow()
                score.add_score()
                food.set_random_pos()
            # gameover check
            if c.is_collided_with_wall(snake) or c.is_collided_with_tail(snake):
                is_gameover = True
                score.display_gameover()
                print("GAME OVER!!!")
        else:
            score.display_paused()
        # frame update and input control
        update_screen()


def update_screen():
    """updates screen visual and input keys"""
    time.sleep(CLOCK_TICK)
    SCREEN.update()


def check_gameover_and_pause():
    global is_gameover
    global is_paused

    if is_gameover:
        restart_game()
    else:
        toggle_pause()


def restart_game():
    """Only works when gameover is True"""
    # clear screen
    SCREEN.clear()
    # reset screen settings
    SCREEN.tracer(0)
    SCREEN.setup(width=LENGTH_X_Y + BLOCK_SIZE, height=LENGTH_X_Y + BLOCK_SIZE)
    SCREEN.bgcolor("#000000")
    SCREEN.title("Snake Game")
    # start game
    game()


def toggle_pause():
    global is_paused
    is_paused = not is_paused


if __name__ == '__main__':
    restart_game()
    SCREEN.exitonclick()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

#TODO #1 CREATE SNAKE BODY

#TODO #2 MOVE THE SNAKE

#TODO #3 CONTROL THE SNAKE

#TODO #4 DETECT COLLISION WITH FOOD

#TODO #5 CREATE A SCOREBOARD

#TODO #6 DETECT COLLISION WITH WALL

#TODO #7 DETECT COLLISION WITH TAIL
