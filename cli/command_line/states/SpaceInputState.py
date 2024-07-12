from .State import State

class SpaceInputState(State):
    def command_input(self) -> None:
        from .CommandInputState import CommandInputState

        context = self.get_context()
        key = context.get_key()

        context.space_key()

        context.transition_to(CommandInputState())

    def check_command_input(self) -> None:
        pass