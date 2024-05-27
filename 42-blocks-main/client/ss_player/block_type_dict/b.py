B0 = [[1], [1]]
B2 = [[1, 1]]


def create_block_type_dict_b() -> dict[str, list[int]]:
    block_type_dict = {}
    block_type_dict["B0"] = B0
    block_type_dict["B2"] = B2

    return block_type_dict


if __name__ == "__main__":
    print(create_block_type_dict_b())
