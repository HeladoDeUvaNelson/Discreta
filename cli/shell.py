import curses
from collections import deque
from .command_line.CommandLine import CommandLine

queue = deque()
current_command = "start"

def enter_is_terminate(x):
    if x == 10 or x == '\n':
        return 7
    return x

def shell(stdscr):
    from .command_line.states.CommandInputState import CommandInputState
    pad = curses.newpad(3, curses.COLS)
    commands_line = CommandLine(CommandInputState(), stdscr, pad)
    commands_line.run()
    
curses.wrapper(shell)