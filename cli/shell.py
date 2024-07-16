import curses
from collections import deque
from .command_line.CommandLine import CommandLine

queue = deque()
current_command = "start"

def shell(stdscr):
    from .command_line.states.CommandInputState import CommandInputState
    main_win = curses.newwin(curses.LINES-3, curses.COLS, 0, 0)
    pad = curses.newpad(3, curses.COLS)

    commands_line = CommandLine(CommandInputState(), stdscr, pad, main_win)
    commands_line.run()