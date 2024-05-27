K0 = [[0, 1], [0, 1], [0, 1], [1, 1]]
K1 = [[1, 0], [1, 0], [1, 0], [1, 1]]
K2 = [[1, 0, 0, 0], [1, 1, 1, 1]]
K3 = [[0, 0, 0, 1], [1, 1, 1, 1]]
K4 = [[1, 1], [1, 0], [1, 0], [1, 0]]
K5 = [[1, 1], [0, 1], [0, 1], [0, 1]]
K6 = [[1, 1, 1, 1], [0, 0, 0, 1]]
K7 = [[1, 1, 1, 1], [1, 0, 0, 0]]


def create_block_type_dict_k() -> dict[str, list[int]]:
    block_type_dict = {}
    block_type_dict["K0"] = K0
    block_type_dict["K1"] = K1
    block_type_dict["K2"] = K2
    block_type_dict["K3"] = K3
    block_type_dict["K4"] = K4
    block_type_dict["K5"] = K5
    block_type_dict["K6"] = K6
    block_type_dict["K7"] = K7

    return block_type_dict


if __name__ == "__main__":
    print(create_block_type_dict_k())
