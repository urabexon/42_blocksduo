R0 = [[1, 1, 0], [0, 1, 1], [0, 0, 1]]
R1 = [[0, 1, 1], [1, 1, 0], [1, 0, 0]]
R2 = [[0, 0, 1], [0, 1, 1], [1, 1, 0]]
R3 = [[1, 0, 0], [1, 1, 0], [0, 1, 1]]


def create_block_type_dict_r() -> dict[str, list[int]]:
    block_type_dict = {}
    block_type_dict["R0"] = R0
    block_type_dict["R1"] = R1
    block_type_dict["R2"] = R2
    block_type_dict["R3"] = R3

    return block_type_dict


if __name__ == "__main__":
    print(create_block_type_dict_r())
