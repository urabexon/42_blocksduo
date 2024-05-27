F0 = [[0, 1], [0, 1], [1, 1]]
F1 = [[1, 0], [1, 0], [1, 1]]
F2 = [[1, 0, 0], [1, 1, 1]]
F3 = [[0, 0, 1], [1, 1, 1]]
F4 = [[1, 1], [1, 0], [1, 0]]
F5 = [[1, 1], [0, 1], [0, 1]]
F6 = [[1, 1, 1], [0, 0, 1]]
F7 = [[1, 1, 1], [1, 0, 0]]


def create_block_type_dict_f() -> dict[str, list[int]]:
    block_type_dict = {}
    block_type_dict["F0"] = F0
    block_type_dict["F1"] = F1
    block_type_dict["F2"] = F2
    block_type_dict["F3"] = F3
    block_type_dict["F4"] = F4
    block_type_dict["F5"] = F5
    block_type_dict["F6"] = F6
    block_type_dict["F7"] = F7

    return block_type_dict


if __name__ == "__main__":
    print(create_block_type_dict_f())
