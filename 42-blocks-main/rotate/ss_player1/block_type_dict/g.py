G0 = [[1, 0], [1, 1], [1, 0]]
G1 = [[0, 1], [1, 1], [0, 1]]
G2 = [[1, 1, 1], [0, 1, 0]]
G6 = [[0, 1, 0], [1, 1, 1]]


def create_block_type_dict_g() -> dict[str, list[int]]:
    block_type_dict = {}
    block_type_dict["G0"] = G0
    block_type_dict["G1"] = G1
    block_type_dict["G2"] = G2
    block_type_dict["G6"] = G6

    return block_type_dict


if __name__ == "__main__":
    print(create_block_type_dict_g())
