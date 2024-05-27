def random_choice(board, pnum, block_list):
    board_list = board_str_to_list(board, pnum)
    # if (no ans) -> (ret = 'X000"), (use_block = 'AA')
    ret, use_block = get_ans(board_list, block_list)
    return ret, use_block
