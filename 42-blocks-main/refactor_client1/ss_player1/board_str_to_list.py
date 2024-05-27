def board_str_to_list(board, pnum):
    my_stone = "o"
    opp_stone = "x"
    if pnum == 2:
        my_stone = "x"
        opp_stone = "o"
    lines = board.splitlines()
    board_list = [3] * 256
    for i in range(1, 15):
        for j in range(0, 15):
            if lines[i][j] == ".":
                board_list[i * 16 + j] = 0
            elif lines[i][j] == my_stone:
                board_list[i * 16 + j] = 1
            elif lines[i][j] == opp_stone:
                board_list[i * 16 + j] = 2
    return board_list
