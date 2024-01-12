from classes.board import Board
from classes.ship import SHIPS_PER_GAME
from classes.player import Player, HumanPlayer, EasyComputerPlayer
from constants.str_coordinates import StringCoordinate
from utils import init_log_record, logger
from utils.args import Args
from utils.terminal_utils import clear_screen

from itertools import cycle
from random import randint


coord_row = [x.name for x in list(StringCoordinate)]


def print_coord_row():
    print('\t' + ' '.join(coord.center(3) for coord in coord_row))


def render_player_board(board: list[str]):
    middle_line = False
    counter = 0
    for row in board:
        if middle_line:
            print('\t' + row)
        else:
            print(f'{10 - counter}\t' + row)
            counter += 1
        middle_line = not middle_line


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
            except Exception as e:
                logger.exception(e)
                logger.info("Try again")
                if isinstance(player, HumanPlayer):
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
        defender = next(turns)
        hit = attacking_player.attack(defender)

        if hit:
            logger.info("Hit!")
            if defender.has_lost():
                logger.info(f"{attacking_player} wins!")
                game_over = True

        attacking_player = defender


if __name__ == '__main__':
    main()
