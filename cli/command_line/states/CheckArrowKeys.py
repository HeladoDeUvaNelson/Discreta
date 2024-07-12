import curses
from .State import State
from .CommandInputState import CommandInputState

class CheckArrowKeys(State):
    def command_input(self) -> None:
        context = self.get_context()
        pad = context.get_pad()
        keys = context.get_keys()
        key = context.get_key()

        key = context.get_input()
        if key == 91:
            key = context.get_input()
            if key == 68 and context.get_pad().getyx()[1] > context.get_root_cursor_signal_yx()[1]: ##Left arrow
                context.move_cursor_left()
                return context.transition_to(CommandInputState())

        context.transition_to(CommandInputState())

    def check_command_input(self) -> None:
        pass

