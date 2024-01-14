from enum import Enum

from classes.player import ComputerPlayer, BeginnerComputerPlayer, SmartComputerPlayer
from errors.input_exceptions import InvalidDifficultyException


class AIPlayerDifficulty(Enum):
    EASY = 1
    MEDIUM = 2
    # HARD = 3

    @staticmethod
    def generate_player(difficulty: "AIPlayerDifficulty") -> ComputerPlayer:
        match difficulty:
            case AIPlayerDifficulty.EASY:
                return BeginnerComputerPlayer()
            case AIPlayerDifficulty.MEDIUM:
                return SmartComputerPlayer()
            case _:
                raise InvalidDifficultyException(difficulty)
