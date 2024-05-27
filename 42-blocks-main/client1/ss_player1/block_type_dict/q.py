Q0 = [[1, 0, 0], [1, 0, 0], [1, 1, 1]]
Q1 = [[0, 0, 1], [0, 0, 1], [1, 1, 1]]
Q2 = [[1, 1, 1], [1, 0, 0], [1, 0, 0]]
Q3 = [[1, 1, 1], [0, 0, 1], [0, 0, 1]]


def create_block_type_dict_q() -> dict[str, list[int]]:
    block_type_dict = {}
    block_type_dict["Q0"] = Q0
    block_type_dict["Q1"] = Q1
    block_type_dict["Q2"] = Q2
    block_type_dict["Q3"] = Q3

    return block_type_dict


if __name__ == "__main__":
    print(create_block_type_dict_q())
