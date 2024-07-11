from .State import State
from .CheckCommandInputState import CheckCommandInputState
from .CheckArrowKeys import CheckArrowKeys

class CheckCommandInputKeyState(State):
    def command_input(self) -> None:
        from .CommandInputState import CommandInputState

        context = self.get_context()
        key = context.get_key()

        command = commands.get(key)

        if command: return command(self)

        context.add_key(key)
        context.transition_to(CommandInputState())

    def check_command_input(self) -> None:
        pass


commands = {
    10: lambda self: self.get_context().transition_to(CheckCommandInputState()), ## Enter.
    27: lambda self: self.get_context().transition_to(CheckArrowKeys()), ## First arrow key ord.
}