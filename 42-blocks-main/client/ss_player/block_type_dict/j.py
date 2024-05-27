J0 = [[1], [1], [1], [1], [1]]
J2 = [[1, 1, 1, 1, 1]]


def create_block_type_dict_j() -> dict[str, list[int]]:
    block_type_dict = {}
    block_type_dict["J0"] = J0
    block_type_dict["J2"] = J2

    return block_type_dict


if __name__ == "__main__":
    print(create_block_type_dict_j())
