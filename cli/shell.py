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
    # terminal_win = curses.newwin(root_win_y-3, root_win_x, 0, 0)
    # terminal_win.border()
    # terminal_win.refresh()

    pad = curses.newpad(3, root_win_x)
    pad.border()
    # text_box_pad = Textbox(pad)
    # text_box_pad.edit(enter_is_terminate)
    key = ''
    string = ""
    pad.addstr(1, 1, ">> ")
    pad.refresh(0, 0, root_win_y-3, 0, root_win_y, root_win_x)
    test = [0, pad.getmaxyx()[1]]
    while True:
        key = pad.getch(1, pad.getyx()[1])
        if key == 10: continue
        if key == '\n': continue

        if key == 127:
            if test[0] > 0: test[0] -= 1
            string = string[:-pad.getyx()[0]]
            if test[0] >= pad.getmaxyx()[1] - 5:
                pad.addstr(1, 1, f">> {string[test[0] - (pad.getmaxyx()[1] - 5):]}")
            else:
                pad.addstr(1, 1, f">> {string}")
            pad.clrtoeol()
            pad.border()
            pad.refresh(0, 0, root_win_y-3, 0, root_win_y, root_win_x)
            continue

        test[0] += 1
        string += chr(key)

        if test[0] >= pad.getmaxyx()[1] - 5: 
            pad.addstr(1, 1, ">> " + string[test[0] - (pad.getmaxyx()[1] - 5):])
            pad.refresh(0, 0, root_win_y-3, 0, root_win_y, root_win_x)
            continue

        pad.addstr(1, 1, ">> " + string)
        pad.refresh(0, 0, root_win_y-3, 0, root_win_y, root_win_x)

    raise Exception("string")

    # command_line_win = curses.newwin(0, 0, root_win_y-3, 0)

    # command_line_text_win = curses.newwin(1, root_win_x-6, root_win_y-2, 4)
    # # curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    # # GREEN_AND_BLACK = curses.color_pair(1)
    # command_line_text_win.deleteln()
    # command_line_text_win.refresh()

    # command_line_win.border()
    # command_line_win_text_box = Textbox(command_line_text_win)

    # command_line_win.addstr(1, 1, ">> ")
    # command_line_win.refresh()

    # command_line_win_text_box.edit(enter_is_terminate)
    
    

    

# def shell():
#     global current_command
#     while current_command != "exit":
#         queue.append(input(">> "))
#         current_command = command_map[queue.pop()]()