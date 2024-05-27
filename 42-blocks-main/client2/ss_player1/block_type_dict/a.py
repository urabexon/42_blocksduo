A0 = [[1]]


def create_block_type_dict_a() -> dict[str, list[int]]:
    block_type_dict = {}
    block_type_dict["A0"] = A0

    return block_type_dict


if __name__ == "__main__":
    print(create_block_type_dict_a())
