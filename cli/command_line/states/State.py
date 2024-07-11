from abc import ABC, abstractmethod
from lombok import Getter, Setter

@Getter
@Setter
class State(ABC):
    _context = None

    @abstractmethod
    def command_input(self) -> None:
        pass

    @abstractmethod
    def check_command_input(self) -> None:
        pass