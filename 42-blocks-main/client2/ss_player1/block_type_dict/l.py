L0 = [[0, 1], [0, 1], [1, 1], [1, 0]]
L1 = [[1, 0], [1, 0], [1, 1], [0, 1]]
L2 = [[1, 1, 0, 0], [0, 1, 1, 1]]
L3 = [[0, 0, 1, 1], [1, 1, 1, 0]]
L4 = [[0, 1], [1, 1], [1, 0], [1, 0]]
L5 = [[1, 0], [1, 1], [0, 1], [0, 1]]
L6 = [[1, 1, 1, 0], [0, 0, 1, 1]]
L7 = [[0, 1, 1, 1], [1, 1, 0, 0]]


def create_block_type_dict_l() -> dict[str, list[int]]:
    block_type_dict = {}
    block_type_dict["L0"] = L0
    block_type_dict["L1"] = L1
    block_type_dict["L2"] = L2
    block_type_dict["L3"] = L3
    block_type_dict["L4"] = L4
    block_type_dict["L5"] = L5
    block_type_dict["L6"] = L6
    block_type_dict["L7"] = L7

    return block_type_dict


if __name__ == "__main__":
    print(create_block_type_dict_l())
