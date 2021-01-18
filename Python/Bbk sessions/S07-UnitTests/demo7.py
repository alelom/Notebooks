def queen_move(x1, y1, x2, y2):
    if x1 < 1 or y1 < 1 or x2 < 1 or y2 < 1 or x1 > 8 or y1 > 8 or x2 > 8 or y2 > 8:
        raise ValueError("Incorrect coordinates specified.")
    if x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1-y2):
        return True
    else:
        return False


if __name__ == "__main__":
    # This basically calls the following lines only if run from command line,
    # not when run by pytest. Useful for development.
    print(queen_move(4, 2, 6, 3))  # invalid
    print(queen_move(4, 1, 4, 3))  # valid vertical
    print(queen_move(2, 2, 3, 2))  # valid horizontal
    print(queen_move(4, 4, 6, 6))  # valid diagonal
