T0 = [[1, 0, 0], [1, 1, 1], [0, 1, 0]]
T1 = [[0, 0, 1], [1, 1, 1], [0, 1, 0]]
T2 = [[0, 1, 1], [1, 1, 0], [0, 1, 0]]
T3 = [[1, 1, 0], [0, 1, 1], [0, 1, 0]]
T4 = [[0, 1, 0], [1, 1, 1], [0, 0, 1]]
T5 = [[0, 1, 0], [1, 1, 1], [1, 0, 0]]
T6 = [[0, 1, 0], [0, 1, 1], [1, 1, 0]]
T7 = [[0, 1, 0], [1, 1, 0], [0, 1, 1]]


def create_block_type_dict_t() -> dict[str, list[int]]:
    block_type_dict = {}
    block_type_dict["T0"] = T0
    block_type_dict["T1"] = T1
    block_type_dict["T2"] = T2
    block_type_dict["T3"] = T3
    block_type_dict["T4"] = T4
    block_type_dict["T5"] = T5
    block_type_dict["T6"] = T6
    block_type_dict["T7"] = T7

    return block_type_dict


if __name__ == "__main__":
    print(create_block_type_dict_t())
