D0 = [[1, 0], [1, 1]]
D1 = [[0, 1], [1, 1]]
D2 = [[1, 1], [1, 0]]
D3 = [[1, 1], [0, 1]]
D4 = [[1, 1], [0, 1]]


def create_block_type_dict_d() -> dict[str, list[int]]:
    block_type_dict = {}
    block_type_dict["D0"] = D0
    block_type_dict["D1"] = D1
    block_type_dict["D2"] = D2
    block_type_dict["D3"] = D3

    return block_type_dict


if __name__ == "__main__":
    print(create_block_type_dict_d())
