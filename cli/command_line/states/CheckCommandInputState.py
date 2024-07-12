from .State import State
from .ExitState import ExitState
import curses
class CheckCommandInputState(State):
    def command_input(self) -> None:
        from .CommandInputState import CommandInputState
        
        context = self.get_context()
        key = context.get_key()

        keys = context.get_keys()

        string = ""
        for key in keys: string += chr(key)
        
        command = commands.get(string.strip())
        
        if command: return command(self)
        context.get_main_win().addstr(1, 2, f"{string}") 
        context.refresh_main_win()

        context.transition_to(CommandInputState())

    def check_command_input(self) -> None:
        pass


commands = {
    "exit": lambda self: self.get_context().transition_to(ExitState())
}