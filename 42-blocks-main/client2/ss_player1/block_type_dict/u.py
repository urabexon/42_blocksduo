U0 = [[0, 1, 0], [1, 1, 1], [0, 1, 0]]


def create_block_type_dict_u() -> dict[str, list[int]]:
    block_type_dict = {}
    block_type_dict["U0"] = U0

    return block_type_dict


if __name__ == "__main__":
    print(create_block_type_dict_u())
