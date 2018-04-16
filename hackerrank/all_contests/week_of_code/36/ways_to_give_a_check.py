#!/bin/python3

# https://www.hackerrank.com/contests/w36/challenges/ways-to-give-a-check

import sys

POSSIBLE, HIDDEN, IMPOSSIBLE = 0, 1, 2

def sign(val):
    if not val:
        return 0
    return int(val / abs(val))

def can_rook_check(board, k_row, k_col, P_row, P_col):
    d_row, d_col = k_row - P_row, k_col - P_col
    if d_row * d_col != 0:
        return IMPOSSIBLE
    # Check line-of-sight
    num_white_pawns = 0
    if d_row == 0:
        # Horizontal
        for i in range(P_col + sign(d_col), k_col, sign(d_col)):
            elem = board[P_row][0][i]
            if elem == 'P':
                num_white_pawns += 1
                if num_white_pawns > 1:
                    return IMPOSSIBLE
            elif elem.isalpha():
                return IMPOSSIBLE
        return num_white_pawns
    else:
        # Vertical
        for i in range(P_row + sign(d_row), k_row, sign(d_row)):
            elem = board[i][0][P_col]
            if elem == 'P':
                num_white_pawns += 1
                if num_white_pawns > 1:
                    return IMPOSSIBLE
            elif elem.isalpha():
                return IMPOSSIBLE
        return num_white_pawns
    return IMPOSSIBLE

def can_bishop_check(board, k_row, k_col, P_row, P_col):
    d_row, d_col = k_row - P_row, k_col - P_col
    if abs(d_row) != abs(d_col):
        return IMPOSSIBLE
    # Check line-of-sight
    num_white_pawns = 0
    for i, j in zip(range(P_row + sign(d_row), k_row, sign(d_row)),
                    range(P_col + sign(d_col), k_col, sign(d_col))):
        elem = board[i][0][j]
        if elem == 'P':
            num_white_pawns += 1
            if num_white_pawns > 1:
                return IMPOSSIBLE
        elif elem.isalpha():
            return IMPOSSIBLE
    return num_white_pawns

def is_discovered_check(board, k_row, k_col, rooks, bishops, queens):
    for rook in rooks:
        if can_rook_check(board, k_row, k_col, rook[0], rook[1]) == POSSIBLE:
            return True
    for bishop in bishops:
        if can_bishop_check(board, k_row, k_col, bishop[0], bishop[1]) == POSSIBLE:
            return True
    for queen in queens:
        if can_rook_check(board, k_row, k_col, queen[0], queen[1]) == POSSIBLE or \
           can_bishop_check(board, k_row, k_col, queen[0], queen[1]) == POSSIBLE:
            return True
    return False

def can_knight_check(board, k_row, k_col, P_row, P_col):
    d_row, d_col = abs(k_row - P_row), abs(k_col - P_col)
    return d_row == 2 * d_col or d_col == 2 * d_row

def waysToGiveACheck(board, k_row, k_col):
    # Complete this function
    # NOTE: board[0]: 8-th rank, board[1]: 7-th rank
    rooks, bishops, queens = [], [], []
    # knights, kings = [], []
    for i in range(8):
        for j in range(8):
            elem = board[i][0][j]
            if elem == 'R':
                # print('found rook')
                if can_rook_check(board, k_row, k_col, i, j) == HIDDEN:
                    rooks.append((i, j))
            elif elem == 'B':
                if can_bishop_check(board, k_row, k_col, i, j) == HIDDEN:
                    bishops.append((i, j))
            elif elem == 'Q':
                if can_rook_check(board, k_row, k_col, i, j) == HIDDEN or \
                    can_bishop_check(board, k_row, k_col, i, j) == HIDDEN:
                    queens.append((i, j))
            # Knights and Kings will not render 'discovered check'
    num_ways = 0
    for i in range(8):
        if board[1][0][i] != 'P':
            continue
        if board[0][0][i].isalpha():
            continue
        P_row, P_col = 0, i
        board_temp = [row[:] for row in board]
        board_temp[P_row][0] = board_temp[P_row][0][:P_col] + 'P' + board_temp[P_row][0][P_col + 1:]
        board_temp[P_row + 1][0] = board_temp[P_row + 1][0][:P_col] + '#' + board_temp[P_row + 1][0][P_col + 1:]
        if is_discovered_check(board_temp, k_row, k_col, rooks, bishops, queens):
            num_ways += 4
            continue
        if can_rook_check(board_temp, k_row, k_col, P_row, P_col) == POSSIBLE or \
           can_bishop_check(board_temp, k_row, k_col, P_row, P_col) == POSSIBLE:
            # Why +2? Queen
            num_ways += 2
            continue
        if can_knight_check(board_temp, k_row, k_col, P_row, P_col):
            num_ways += 1
            continue
    return num_ways

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        board = []
        for board_i in range(8):
           board_t = [str(board_temp) for board_temp in input().strip().split(' ')]
           board.append(board_t)
           if 'k' in board_t[0]:
               k_row = board_i
               k_col = board_t[0].find('k')
        result = waysToGiveACheck(board, k_row, k_col)
        print(result)
