from collections import deque
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
    i = 0
    last = []
    while True:
        key = pad.getch(1, pad.getyx()[1])

        if key == 10: continue ## enter
        if key == '\n': continue ## breakline?
        # if key == 113: break ## q
        
        i += 1  

        ## arrow keys
        if key == 27:
            key = pad.getch(1, pad.getyx()[1])
            if key == 91:
                key = pad.getch(1, pad.getyx()[1])
                if test[0] > 0:
                    if key == 68 and curses.getsyx()[1] > 4: 
                        curses.setsyx(root_win_y-2, curses.getsyx()[1]-1 if test[0] > 0 else 0)
                        curses.doupdate()
                    if key == 67 and curses.getsyx()[1]-4 < test[0]: 
                        curses.setsyx(root_win_y-2, curses.getsyx()[1]+1)
                        curses.doupdate()
                continue

        
        ## return
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

    raise Exception(i)