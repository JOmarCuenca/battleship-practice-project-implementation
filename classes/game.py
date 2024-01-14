from classes.board import Board
from classes.player import Player, HumanPlayer
from errors.game_exceptions import OngoingGameException
from errors.input_exceptions import UnknownGameObjectException

from itertools import cycle
from pickle import dumps, loads, UnpicklingError


class Game:
    player_1: Player
    player_2: Player
    boards = list[tuple[Board, Board]]
    finished = False
    paused = False
    _turns = None

    player_1_wins = 0
    player_2_wins = 0

    def __init__(self, player_1: Player, player_2: Player):
        self.player_1 = player_1
        self.player_2 = player_2
        self.boards = []
        self._turns = cycle([self.player_1, self.player_2])

    @property
    def total_games_played(self) -> int:
        total = len(self.boards)

        if not self.finished:
            total += 1

        return total

    @property
    def game_score(self) -> tuple[int, int]:
        return self.player_1_wins, self.player_2_wins

    @property
    def winner(self) -> Player:
        if not self.finished:
            raise OngoingGameException()

        if self.player_1_wins > self.player_2_wins:
            return self.player_1

        return self.player_2

    def contains_humans(self) -> bool:
        return isinstance(self.player_1, HumanPlayer) or isinstance(self.player_2, HumanPlayer)

    def next_turn(self) -> Player:
        return next(self._turns)

    def finish_game_set(self, player: Player):
        self.boards.append((self.player_1.board, self.player_2.board))
        self.finished = True
        self.paused = False

        if player is self.player_1:
            self.player_1_wins += 1
        else:
            self.player_2_wins += 1

    def reset_game_set(self):
        self.player_1.reset_board()
        self.player_2.reset_board()
        self.finished = False
        self._turns = cycle([self.player_1, self.player_2])

    def pause_game_set(self):
        self.paused = True
        return dumps(self)

    @staticmethod
    def resume_game_set(game_state: bytes) -> 'Game':
        loaded_game = None

        try:
            loaded_game = loads(game_state)
        except UnpicklingError as e:
            raise UnknownGameObjectException() from e

        if not isinstance(loaded_game, Game):
            raise UnknownGameObjectException()

        # Skip a turn so that the next turn is the correct player
        loaded_game.next_turn()

        return loaded_game
