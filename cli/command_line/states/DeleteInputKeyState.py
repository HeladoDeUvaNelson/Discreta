from .State import State

class DeleteInputKeyState(State):
    def command_input(self) -> None:
        from .CommandInputState import CommandInputState

        context = self.get_context()
        context.delete_key()

        context.transition_to(CommandInputState())

    def check_command_input(self) -> None:
        pass