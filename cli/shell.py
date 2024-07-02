from collections import deque
# from .commands.commandmap import command_map
import curses
from curses import wrapper
from curses.textpad import Textbox, rectangle

queue = deque()
current_command = "start"

def enter_is_terminate(x):
    if x == 10 or x == '\n':
        return 7
    return x

def shell(stdscr):
    root_win_y = curses.LINES
    root_win_x = curses.COLS

    terminal_win = curses.newwin(root_win_y-3, root_win_x, 0, 0)
    terminal_win.border()
    terminal_win.refresh()

    command_line_win = curses.newwin(0, 0, root_win_y-3, 0)
    # curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    # GREEN_AND_BLACK = curses.color_pair(1)
    command_line_win.border()
    command_line_win_text_box = Textbox(command_line_win)
    command_line_win.addstr(1, 1, ">> ")
    command_line_win_text_box.edit(enter_is_terminate)
    command_line_win.refresh()

    

# def shell():
#     global current_command
#     while current_command != "exit":
#         queue.append(input(">> "))
#         current_command = command_map[queue.pop()]()