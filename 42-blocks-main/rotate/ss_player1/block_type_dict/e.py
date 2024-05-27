E0 = [[1], [1], [1], [1]]
E2 = [[1, 1, 1, 1]]


def create_block_type_dict_e() -> dict[str, list[int]]:
    block_type_dict = {}
    block_type_dict["E0"] = E0
    block_type_dict["E2"] = E2

    return block_type_dict


if __name__ == "__main__":
    print(create_block_type_dict_e())
