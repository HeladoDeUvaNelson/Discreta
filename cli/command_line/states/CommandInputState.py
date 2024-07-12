from .State import State
import curses

class CommandInputState(State):
    def command_input(self) -> None:
        from .CheckCommandInputKeyState import CheckCommandInputKeyState
        context = self.get_context()
        
        context.refresh_input()
        
        context.set_key(context.get_input())  
        context.get_root_win()().addstr(0, 0, f"pad input pos {curses.LINES-context.get_pad().getyx()[0]} {context.get_pad().getyx()[1]}")   
        context.get_root_win()().addstr(1, 0, f"pad input pos {context.get_head_pos()}")
        context.transition_to(CheckCommandInputKeyState())
        
    def check_command_input(self) -> None:
        pass