import curses
import os

os.system("cls" if os.name == "nt" else "clear")
import random
import curses

screen = curses.initscr()
curses.curs_set(0)
max_height, max_width = screen.getmaxyx()
new_window = curses.newwin(max_height, max_width, 0, 0)
new_window.keypad(1)
new_window.timeout(120)
snk_x = max_width // 4
snk_y = max_height // 2
snake = [[snk_y, snk_x], [snk_y, snk_x - 1], [snk_y, snk_x - 2]]
food = [max_height // 2, max_width // 2]
new_window.addch(food[0], food[1], curses.ACS_PI)
key = curses.KEY_RIGHT
while True:
    next_key = new_window.getch()
    key = key if next_key == -1 else next_key

    new_head = [snake[0][0], snake[0][1]]
    if key == curses.KEY_UP:
        new_head[0] -= 1
    if key == curses.KEY_DOWN:
        new_head[0] += 1
    if key == curses.KEY_LEFT:
        new_head[1] -= 1
    if key == curses.KEY_RIGHT:
        new_head[1] += 1

    snake.insert(0, new_head)

    if (
        snake[0][0] in [0, max_height]
        or snake[0][1] in [0, max_width]
        or snake[0] in snake[1:]
    ):
        curses.endwin()
        quit()

    if snake[0] == food:
        food = None
        while food is None:
            new_food = [
                random.randint(1, max_height - 1),
                random.randint(1, max_width - 1),
            ]
            if new_food not in snake:
                food = new_food
        new_window.addch(food[0], food[1], curses.ACS_PI)
    else:
        tail = snake.pop()
        new_window.addch(tail[0], tail[1], " ")
    new_window.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)
