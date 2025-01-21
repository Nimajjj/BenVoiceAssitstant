from enum import Enum


class Action(Enum):
    UNKNOWN = -1
    QUIT = 0
    WEATHER = 1
    MUSIC = 2
    EMAIL = 3
    SEARCH = 4

    @staticmethod
    def from_str(act: str):
        act = act.strip().lower()
        if act == "quit":
            return Action.QUIT
        if act == "weather":
            return Action.WEATHER
        if act == "music":
            return Action.MUSIC
        if act == "email":
            return Action.EMAIL
        if act == "search":
            return Action.SEARCH
        return Action.UNKNOWN
    
    def to_str(self) -> str:
        return f"{self.__class__.__name__}.{self.name}"

class Strategy:
    def __init__(self, action: Action, data: dict):
        self.action = action
        self.data = data

    def __str__(self):
        return f"Strategy(action={self.action.name}, data={self.data})"