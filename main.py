from classes.board import Board
from classes.ship import SHIPS_PER_GAME
from classes.player import Player, HumanPlayer, EasyComputerPlayer
from constants.str_coordinates import StringCoordinate
from errors.input_exceptions import InvalidInputException
from errors.board_exceptions import GameBoardException
from utils import init_log_record, logger
from utils.args import Args
from utils.terminal_utils import clear_screen

from itertools import cycle
from random import randint


coord_row = [x.name for x in list(StringCoordinate)]

BOARD_LEFT_SPACE = 43


def get_coord_row():
    return ' '.join(coord.center(3) for coord in coord_row)


def print_coord_row():
    print(get_coord_row().rjust(BOARD_LEFT_SPACE))


def print_double_coord_row():
    print(get_coord_row().rjust(BOARD_LEFT_SPACE) +
          get_coord_row().rjust(BOARD_LEFT_SPACE))


def render_player_board(board: list[str]):
    middle_line = False
    counter = 0
    for row in board:
        if middle_line:
            print(row.rjust(BOARD_LEFT_SPACE))
        else:
            space = 3
            print(f'{10 - counter}'.rjust(space) +
                  row.rjust(BOARD_LEFT_SPACE - space) + f'{10 - counter}'.ljust(space))

            counter += 1
        middle_line = not middle_line


def render_game_vertical(board_1: Board, board_2: Board):
    print_coord_row()

    render_player_board(board_1.opponent_lines())

    print_coord_row()

    render_player_board(board_2.player_lines())

    print_coord_row()


def render_game_horizontal(board_1: Board, board_2: Board):

    print_double_coord_row()

    left, right = board_1.player_lines(), board_2.opponent_lines()

    middle_line = False
    counter = 0
    space = 3

    for left_row, right_row in zip(left, right):
        if middle_line:
            print(left_row.rjust(BOARD_LEFT_SPACE) +
                  right_row.rjust(BOARD_LEFT_SPACE))
        else:
            print(f'{10 - counter}'.rjust(space) +
                  left_row.rjust(BOARD_LEFT_SPACE - space) + f'{10 - counter}'.center(space) + right_row.rjust(BOARD_LEFT_SPACE - space) + f'{10 - counter}'.ljust(space))

            counter += 1
        middle_line = not middle_line

    print_double_coord_row()


def place_ships(player: Player):
    for ship in SHIPS_PER_GAME:
        ready = False
        while not ready:
            try:
                if isinstance(player, HumanPlayer):
                    clear_screen()
                    render_player_board(player.board.player_lines())
                    print_coord_row()
                player.place_ship(ship)
                ready = True
            except (InvalidInputException, GameBoardException) as e:
                logger.error(e)
                if isinstance(player, HumanPlayer):
                    logger.info("Try again")
                    input("Press enter to continue")
            except KeyboardInterrupt:
                logger.info("Exiting...")
                exit(0)
            except Exception as e:
                logger.exception(e)
                if isinstance(player, HumanPlayer):
                    logger.info("Try again")
                    input("Press enter to continue")

    if isinstance(player, HumanPlayer):
        clear_screen()
        render_player_board(player.board.player_lines())
        print_coord_row()


def main():
    args = Args.parseArgs()
    init_log_record(args.log_level, args.log_file_extension, args.verbose)

    player = HumanPlayer()

    place_ships(player)
    logger.info("Player ships placed")

    computer = EasyComputerPlayer()
    place_ships(computer)
    logger.info("Computer ships placed")

    if args.log_level == 'DEBUG':
        logger.debug(f"Computer board: {computer.board}")
        clear_screen()
        render_player_board(computer.board.player_lines())
        print_coord_row()

    turns = cycle([player, computer])

    if randint(0, 1) == 1:
        # Computer starts
        next(turns)

    attacking_player = next(turns)

    game_over = False

    while not game_over:
        clear_screen()
        defender = next(turns)
        if args.horizontal:
            render_game_horizontal(attacking_player.board, defender.board)
        else:
            render_game_vertical(attacking_player.board, defender.board)

        hit = False

        try:
            hit = attacking_player.attack(defender)
        except KeyboardInterrupt:
            logger.info("Exiting...")
            exit(0)

        if hit:
            logger.info("Hit!")
            if defender.has_lost():
                logger.info(f"{attacking_player} wins!")
                game_over = True

        attacking_player = defender


if __name__ == '__main__':
    main()
