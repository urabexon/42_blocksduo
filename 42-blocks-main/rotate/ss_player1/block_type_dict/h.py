H0 = [[1, 1], [1, 1]]


def create_block_type_dict_h() -> dict[str, list[int]]:
    block_type_dict = {}
    block_type_dict["H0"] = H0

    return block_type_dict


if __name__ == "__main__":
    print(create_block_type_dict_h())
