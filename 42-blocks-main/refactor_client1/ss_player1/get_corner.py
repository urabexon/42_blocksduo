def is_upper_left_corner(i: int, j: int, board_list: list[list[int]]) -> bool:
    if (2 <= i <= 15) and (2 <= j <= 15):
        if board_list[((i - 1) << 4) + j - 1] == 1:  # (-1, -1)
            return True
    return False


def is_lower_left_corner(i: int, j: int, board_list: list[list[int]]) -> bool:
    if (2 <= i <= 15) and (1 <= j <= 14):
        if board_list[((i - 1) << 4) + j + 1] == 1:  # (-1, +1)
            return True
    return False


def is_upper_right_corner(i: int, j: int, board_list: list[list[int]]) -> bool:
    if (1 <= i <= 14) and (2 <= j <= 15):
        if board_list[((i + 1) << 4) + j - 1] == 1:  # (+1, -1)
            return True
    return False


def is_lower_right_corner(i: int, j: int, board_list: list[list[int]]) -> bool:
    if (1 <= i <= 14) and (1 <= j <= 14):
        if board_list[((i + 1) << 4) + j + 1] == 1:  # (+1, +1)
            return True
    return False


def get_corner(board_list):
    upper_left_corners = []
    lower_left_corners = []
    upper_right_corners = []
    lower_right_corners = []
    for i in range(15):
        for j in range(15):
            if board_list[(i << 4) + j] == 0:
                if is_upper_left_corner(i, j, board_list):
                    upper_left_corners.append((i, j))
                if is_lower_left_corner(i, j, board_list):
                    lower_left_corners.append((i, j))
                if is_upper_right_corner(i, j, board_list):
                    upper_right_corners.append((i, j))
                if is_lower_right_corner(i, j, board_list):
                    lower_right_corners.append(((i, j)))
    return upper_left_corners, lower_left_corners, upper_right_corners, lower_right_corners
