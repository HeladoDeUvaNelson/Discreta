from curses import newpad, newwin, initscr, endwin
import curses
from .lombok import Getter, Setter
from .states.State import State
from .states.CommandInputState import CommandInputState
from .states.ExitState import ExitState

@Getter
@Setter
class CommandLine:
    _state = None
    _root_win: initscr = None
    _root_win_size: tuple = None
    _main_win: newwin = None
    _main_win_size: tuple = None
    _pad: newpad = None
    _pad_size: tuple = None
    _pad_border: bool = True
    _pad_showing_screen = None
    _key: str = None
    _keys: list = []
    _head_pos: int = 0
    _cursor_signal: str = None
    _cursor_signal_yx: tuple = None
    _root_cursor_signal_yx: tuple = None
    _kwargs = {
        "border": {
            "type": bool,
            "set": lambda self: self.set_pad_border
            }
        }

    def __init__(self, state: State, root_win: initscr, pad: newpad, mainwin: newwin, **kwargs) -> None:
        self.transition_to(state)
        self.set_root_win(initscr)
        self.set_pad(pad)
        self.set_main_win(mainwin)
        self.set_cursor_signal(">>", (1, 1))
        y, x = self.get_pad().getyx()
        self.set_root_cursor_signal_yx((curses.LINES-2-y, len(self.get_cursor_signal())+2))
        self.set_head_pos(self.get_root_cursor_signal_yx())

        self._validate_execute_kwargs(kwargs)

    def transition_to(self, state: State):
        self.set_state(state)
        self.get_state().set_context(self)

    def run(self) -> None:
        while not isinstance(self.get_state(), ExitState):
            self.command_input()

    def command_input(self) -> None:
        self.get_state().command_input()

    def get_input(self) -> int:
        return self.get_pad().getch()

    def check_command_input(self) -> None:
        self.get_state().check_command_input()

    def add_key(self, key: int) -> None:
        # if self.get_head_pos()[1] < self.get_pad_size()[1] - self.get_cursor_signal_yx()[1]-1:
        y, x = self.get_head_pos()
        keys = self.get_keys().insert(x - (self.get_root_cursor_signal_yx()[1]), key)
        self.set_head_pos((y, x+1))
        self.refresh_cursor_pos(self.get_head_pos(), False)

    def delete_key(self) -> None:
        if self.get_head_pos()[1] > self.get_root_cursor_signal_yx()[1]:
            del self.get_keys()[self.get_head_pos()[1]-self.get_root_cursor_signal_yx()[1]-1]
            self.move_cursor_left()
            self.refresh_input()
            self.get_pad().clrtoeol()
            

    def space_key(self) -> None:
        # if self.get_head_pos()[1] < self.get_pad_size()[1] - self.get_cursor_signal_yx()[1]-1:
        self.add_key(32)

    def move_cursor_left(self) -> None:
        y, x = self.get_head_pos()
        x -= 1
        if x >= self.get_root_cursor_signal_yx()[1]:
            self.set_head_pos((y, x))
            self.refresh_cursor_pos(self.get_head_pos())

    def move_cursor_right(self) -> None:
        y, x = self.get_head_pos()
        x += 1
        if x <= self.get_pad().getyx()[1]:
            self.set_head_pos((y, x))
            self.refresh_cursor_pos(self.get_head_pos())

    def refresh_input(self) -> None:
        keys = self.get_keys()
        y, x = self.get_cursor_signal_yx()
        pad = self.get_pad()

        string = ""
        for key in keys: string += chr(key)
        str_len = len(string)

        if str_len >= self.get_pad_size()[1] - self.get_root_cursor_signal_yx()[1] - 1:
            pad.addstr(y, x, f"{self.get_cursor_signal()} {string[str_len - (self.get_pad_size()[1] - self.get_root_cursor_signal_yx()[1] - 1):]}")
        else:
            pad.addstr(y, x, f"{self.get_cursor_signal()} {string}")

        self.refresh_pad()

        self.refresh_cursor_pos(self.get_head_pos())
        
    def refresh_cursor_pos(self, yx: tuple, update: bool=True) -> None:
        y, x = yx
        curses.setsyx(y, x)
        if update: curses.doupdate()

    def refresh_pad(self) -> None:
        uly, ulx, ulfy, ulfx, ry, rx = self.get_pad_showing_screen()
        self.get_pad().border() if self.get_pad_border() else "" 
        self.get_pad().refresh(uly, ulx, ulfy, ulfx, ry, rx)

    def refresh_main_win(self) -> None:
        self.get_main_win().border()
        self.get_main_win().refresh()

    def set_root_win(self, root_win):
        self.set_root_win_size((curses.LINES, curses.COLS))
        self._root_win = root_win

    def set_pad(self, pad):
        self.set_pad_size((pad.getmaxyx()[0], pad.getmaxyx()[1]))
        self.set_pad_showing_screen((0, 0, curses.LINES-3, 0, curses.LINES, curses.COLS))
        self._pad = pad

    def set_main_win(self, mainwin):
        self.set_main_win_size((mainwin.getmaxyx()[0], mainwin.getmaxyx()[1]))
        self._main_win = mainwin

    def set_cursor_signal(self, cursor_signal: str, yx: tuple):
        self._cursor_signal_yx = yx
        self._cursor_signal = cursor_signal

    def _validate_execute_kwargs(self, kwargs):
        for key, value in kwargs.items():
            kwarg_function = self.get_kwargs().get(key)
            
            if not kwarg_function: self._raise_exception_error(f"| {key} | parameter is unknown.")
            if kwarg_function.get('type') != type(value): self._raise_exception_error(f"| {value} | parameter value is unknown.")
            
            kwarg_function.get("set")(self)(value)

    def _raise_exception_error(self, mess):
        raise Exception(mess)
