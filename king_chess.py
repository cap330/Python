chess_column = int(input())
chess_row = int(input())
able_move_count = 0


def able_move(new_column, new_row):
    global able_move_count
    if 0< new_column < 9:
        if 0 < new_row < 9:
            able_move_count += 1
            return True
    return False


able_move(chess_column - 1, chess_row - 1)
able_move(chess_column + 1, chess_row + 1)
able_move(chess_column + 1, chess_row)
able_move(chess_column, chess_row + 1)
able_move(chess_column - 1, chess_row)
able_move(chess_column, chess_row - 1)
able_move(chess_column + 1, chess_row - 1)
able_move(chess_column - 1, chess_row + 1)    

print(able_move_count)
