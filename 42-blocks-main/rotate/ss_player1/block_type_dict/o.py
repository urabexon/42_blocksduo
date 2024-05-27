O0 = [[1, 0], [1, 1], [1, 0], [1, 0]]
O1 = [[0, 1], [1, 1], [0, 1], [0, 1]]
O2 = [[1, 1, 1, 1], [0, 0, 1, 0]]
O3 = [[1, 1, 1, 1], [0, 1, 0, 0]]
O4 = [[0, 1], [0, 1], [1, 1], [0, 1]]
O5 = [[1, 0], [1, 0], [1, 1], [1, 0]]
O6 = [[0, 1, 0, 0], [1, 1, 1, 1]]
O7 = [[0, 0, 1, 0], [1, 1, 1, 1]]


def create_block_type_dict_o() -> dict[str, list[int]]:
    block_type_dict = {}
    block_type_dict["O0"] = O0
    block_type_dict["O1"] = O1
    block_type_dict["O2"] = O2
    block_type_dict["O3"] = O3
    block_type_dict["O4"] = O4
    block_type_dict["O5"] = O5
    block_type_dict["O6"] = O6
    block_type_dict["O7"] = O7

    return block_type_dict


if __name__ == "__main__":
    print(create_block_type_dict_o())
