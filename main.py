from classes.board import Board
from classes.game import Game
from classes.ship import SHIPS_PER_GAME
from classes.player import Player, HumanPlayer
from constants.str_coordinates import StringCoordinate
from constants.ai_player_difficulty import AIPlayerDifficulty
from errors.input_exceptions import InvalidInputException, UnknownGameObjectException
from errors.board_exceptions import GameBoardException
from errors.game_exceptions import GameplayException
from utils import init_log_record, logger
from utils.args import Args
from utils.terminal_utils import clear_screen

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

    player.boats_placed = True

    if isinstance(player, HumanPlayer):
        clear_screen()
        render_player_board(player.board.player_lines())
        print_coord_row()


def play(game: Game, horizontal: bool = False) -> Player:

    # Randomly choose who starts if game wasn't started before
    if not game.paused and randint(0, 1) == 1:
        # Player 2 starts
        game.next_turn()

    attacking_player = game.next_turn()

    game_over = False

    while not game_over:
        if game.contains_humans():
            clear_screen()
        defender = game.next_turn()

        if game.contains_humans():
            if horizontal:
                render_game_horizontal(attacking_player.board, defender.board)
            else:
                render_game_vertical(attacking_player.board, defender.board)

        hit = False
        valid = False

        while not valid:
            try:
                hit = attacking_player.attack(defender)
                valid = True
            except GameplayException as e:
                logger.error(e)
                if isinstance(attacking_player, HumanPlayer):
                    logger.info("Try again")
                    input("Press enter to continue")
            except KeyboardInterrupt:
                logger.info("Exiting...")
                exit(0)
            except Exception as e:
                logger.exception(e)
                if isinstance(attacking_player, HumanPlayer):
                    logger.info("Try again")
                    input("Press enter to continue")

        if hit:
            logger.info("Hit!")
            if defender.has_lost():
                logger.info(f"{attacking_player} wins!")
                game_over = True

        if not game_over:
            attacking_player = defender

    logger.debug("Game over")

    return attacking_player


def begin_game(game: Game, number_sets=1, horizontal: bool = False):
    logger.info("Beginning game")

    while not game.finished:

        player_1, player_2 = game.player_1, game.player_2

        if not player_1.boats_placed:
            place_ships(player_1)
            logger.info(f"{player_1} ships placed")

        if not player_2.boats_placed:
            place_ships(player_2)
            logger.info(f"{player_2} ships placed")

        winner = play(game, horizontal)

        clear_screen()
        render_game_horizontal(player_1.board, player_2.board)

        logger.info(f"{winner} wins!")

        game.finish_game_set(winner)

        if not game.contains_humans() and number_sets > 1:
            logger.info("Resetting game set")
            game.reset_game_set()
            number_sets -= 1
            logger.info("Game set reset")

        elif game.contains_humans():
            answer = input("Play again? (y/n): ").lower()

            if answer == 'y':
                logger.info("Resetting game set")
                game.reset_game_set()
                logger.info("Game set reset")


def create_game(pvp: bool, pvc: bool) -> Game:
    player_1, player_2 = HumanPlayer(), None

    try:
        if pvp:
            player_1.name = input("Player 1 name: ")
            player_2 = HumanPlayer()
            player_2.name = input("Player 2 name: ")
        else:
            logger.debug(f"Assigning computer difficulty to {pvc}")
            player_2 = AIPlayerDifficulty.generate_player(pvc)
    except KeyboardInterrupt:
        logger.info("Exiting...")
        exit(0)

    return Game(player_1, player_2)


@logger.catch(reraise=True)
def resume_game(previous_game_path: str) -> Game:
    game = None

    try:
        with open(previous_game_path, 'rb') as file:
            game = Game.resume_game_set(file.read())

    except FileNotFoundError:
        logger.error(f"File {previous_game_path} not found")
        logger.info("Exiting...")
        exit(0)

    except UnknownGameObjectException as e:
        logger.error("The file detected didn't contain a game object")
        logger.info("Exiting...")
        exit(0)

    if game.finished:
        logger.info("Game is finished and paused. Resuming...")
        game.resume_game_set()

    return game


def main():
    args = Args.parseArgs()
    init_log_record(args.log_level, args.log_file_extension, args.verbose)

    game = resume_game(args.previous_game_path) if args.previous_game_path else create_game(
        args.pvp, args.pvc)

    begin_game(game, horizontal=args.horizontal)

    logger.info(f"Total games played: {game.total_games_played}")

    p1_wins, p2_wins = game.game_score

    if p1_wins > p2_wins:
        logger.info(f"{game.player_1} wins the game!")
    elif p2_wins > p1_wins:
        logger.info(f"{game.player_2} wins the game!")
    else:
        logger.info("It's a tie!")

    logger.info("Thanks for playing!")


if __name__ == '__main__':
    main()
