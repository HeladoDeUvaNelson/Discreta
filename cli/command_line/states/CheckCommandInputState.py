from .State import State
from .ExitState import ExitState

class CheckCommandInputState(State):
    def command_input(self) -> None:
        from .CommandInputState import CommandInputState
        
        context = self.get_context()
        key = context.get_key()

        context.add_key(key)

        keys = context.get_keys()

        string = ""
        for key in keys: string += chr(key)
        
        command = commands.get(string)
        
        if command: return command(self)

        context.transition_to(CommandInputState())

    def check_command_input(self) -> None:
        pass


commands = {
    "exit": lambda self: self.get_context().transition_to(ExitState())
}