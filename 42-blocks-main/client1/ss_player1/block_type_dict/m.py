M0 = [[0, 1], [1, 1], [1, 1]]
M1 = [[1, 0], [1, 1], [1, 1]]
M2 = [[1, 1, 0], [1, 1, 1]]
M3 = [[0, 1, 1], [1, 1, 1]]
M4 = [[1, 1], [1, 1], [1, 0]]
M5 = [[1, 1], [1, 1], [0, 1]]
M6 = [[1, 1, 1], [0, 1, 1]]
M7 = [[1, 1, 1], [1, 1, 0]]


def create_block_type_dict_m() -> dict[str, list[int]]:
    block_type_dict = {}
    block_type_dict["M0"] = M0
    block_type_dict["M1"] = M1
    block_type_dict["M2"] = M2
    block_type_dict["M3"] = M3
    block_type_dict["M4"] = M4
    block_type_dict["M5"] = M5
    block_type_dict["M6"] = M6
    block_type_dict["M7"] = M7

    return block_type_dict


if __name__ == "__main__":
    print(create_block_type_dict_m())
