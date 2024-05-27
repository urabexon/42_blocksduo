S0 = [[1, 0, 0], [1, 1, 1], [0, 0, 1]]
S1 = [[0, 0, 1], [1, 1, 1], [1, 0, 0]]
S2 = [[0, 1, 1], [0, 1, 0], [1, 1, 0]]
S3 = [[1, 1, 0], [0, 1, 0], [0, 1, 1]]


def create_block_type_dict_s() -> dict[str, list[int]]:
    block_type_dict = {}
    block_type_dict["S0"] = S0
    block_type_dict["S1"] = S1
    block_type_dict["S2"] = S2
    block_type_dict["S3"] = S3

    return block_type_dict


if __name__ == "__main__":
    print(create_block_type_dict_s())
