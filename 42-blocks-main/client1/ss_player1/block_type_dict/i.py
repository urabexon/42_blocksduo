I0 = [[1, 1, 0], [0, 1, 1]]
I1 = [[0, 1, 1], [1, 1, 0]]
I2 = [[0, 1], [1, 1], [1, 0]]
I3 = [[1, 0], [1, 1], [0, 1]]


def create_block_type_dict_i() -> dict[str, list[int]]:
    block_type_dict = {}
    block_type_dict["I0"] = I0
    block_type_dict["I1"] = I1
    block_type_dict["I2"] = I2
    block_type_dict["I3"] = I3

    return block_type_dict


if __name__ == "__main__":
    print(create_block_type_dict_i())
