N0 = [[1, 1], [0, 1], [1, 1]]
N1 = [[1, 1], [1, 0], [1, 1]]
N2 = [[1, 0, 1], [1, 1, 1]]
N6 = [[1, 1, 1], [1, 0, 1]]


def create_block_type_dict_n() -> dict[str, list[int]]:
    block_type_dict = {}
    block_type_dict["N0"] = N0
    block_type_dict["N1"] = N1
    block_type_dict["N2"] = N2
    block_type_dict["N6"] = N6

    return block_type_dict


if __name__ == "__main__":
    print(create_block_type_dict_n())
