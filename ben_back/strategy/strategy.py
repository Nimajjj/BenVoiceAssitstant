from enum import Enum


class Action(Enum):
    UNKNOWN = -1
    QUIT = 0
    WEATHER = 1
    MUSIC = 2
    EMAIL = 3
    SEARCH = 4


class Strategy:
    def __init__(self, action: Action, data: dict):
        self.action = action
        self.data = data

