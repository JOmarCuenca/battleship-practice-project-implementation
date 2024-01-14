from enum import Enum

from classes.player import ComputerPlayer, BeginnerComputerPlayer, SmartComputerPlayer
from errors.input_exceptions import InvalidDifficultyException


class AIPlayerDifficulty(Enum):
    EASY = "EASY"
    MEDIUM = "MEDIUM"
    # HARD = "HARD"

    @staticmethod
    def generate_player(difficulty: "AIPlayerDifficulty") -> ComputerPlayer:
        match difficulty:
            case AIPlayerDifficulty.EASY:
                return BeginnerComputerPlayer()
            case AIPlayerDifficulty.MEDIUM:
                return SmartComputerPlayer()
            case _:
                raise InvalidDifficultyException(difficulty)
            
    def __str__(self) -> str:
        return self.name.lower()
