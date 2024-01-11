
if __name__ == '__main__':
    from classes.board import Board

    board = Board()
    print("Player board")
    print('\n'.join(board.player_lines()))
    print("Opponent board")
    print('\n'.join(board.opponent_lines()))