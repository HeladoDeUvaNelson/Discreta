from .State import State

class CommandInputState(State):
    def command_input(self) -> None:
        from .CheckCommandInputKeyState import CheckCommandInputKeyState
        
        context = self.get_context()
        context.set_cursor_signal(">>", (1, 1))
        context.refresh_input()
        
        context.set_key(context.get_input())     

        context.transition_to(CheckCommandInputKeyState())
        
    def check_command_input(self) -> None:
        pass