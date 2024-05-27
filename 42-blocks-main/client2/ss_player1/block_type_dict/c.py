C0 = [[1], [1], [1]]
C2 = [[1, 1, 1]]


def create_block_type_dict_c() -> dict[str, list[int]]:
    block_type_dict = {}
    block_type_dict["C0"] = C0
    block_type_dict["C2"] = C2

    return block_type_dict


if __name__ == "__main__":
    print(create_block_type_dict_c())
