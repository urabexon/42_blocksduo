P0 = [[0, 1, 0], [0, 1, 0], [1, 1, 1]]
P2 = [[1, 0, 0], [1, 1, 1], [1, 0, 0]]
P3 = [[0, 0, 1], [1, 1, 1], [0, 0, 1]]
P4 = [[1, 1, 1], [0, 1, 0], [0, 1, 0]]


def create_block_type_dict_p() -> dict[str, list[int]]:
    block_type_dict = {}
    block_type_dict["P0"] = P0
    block_type_dict["P2"] = P2
    block_type_dict["P3"] = P3
    block_type_dict["P4"] = P4

    return block_type_dict


if __name__ == "__main__":
    print(create_block_type_dict_p())
