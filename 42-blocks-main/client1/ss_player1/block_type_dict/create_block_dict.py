import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from ss_player1.block_type_dict.a import create_block_type_dict_a
from ss_player1.block_type_dict.b import create_block_type_dict_b
from ss_player1.block_type_dict.c import create_block_type_dict_c
from ss_player1.block_type_dict.d import create_block_type_dict_d
from ss_player1.block_type_dict.e import create_block_type_dict_e
from ss_player1.block_type_dict.f import create_block_type_dict_f
from ss_player1.block_type_dict.g import create_block_type_dict_g
from ss_player1.block_type_dict.h import create_block_type_dict_h
from ss_player1.block_type_dict.i import create_block_type_dict_i
from ss_player1.block_type_dict.j import create_block_type_dict_j
from ss_player1.block_type_dict.k import create_block_type_dict_k
from ss_player1.block_type_dict.l import create_block_type_dict_l
from ss_player1.block_type_dict.m import create_block_type_dict_m
from ss_player1.block_type_dict.n import create_block_type_dict_n
from ss_player1.block_type_dict.o import create_block_type_dict_o
from ss_player1.block_type_dict.p import create_block_type_dict_p
from ss_player1.block_type_dict.q import create_block_type_dict_q
from ss_player1.block_type_dict.r import create_block_type_dict_r
from ss_player1.block_type_dict.s import create_block_type_dict_s
from ss_player1.block_type_dict.t import create_block_type_dict_t
from ss_player1.block_type_dict.u import create_block_type_dict_u


def create_block_type_dict() -> dict[str, dict[str, list[str]]]:
    block_dict = {}
    block_dict["A"] = create_block_type_dict_a()
    block_dict["B"] = create_block_type_dict_b()
    block_dict["C"] = create_block_type_dict_c()
    block_dict["D"] = create_block_type_dict_d()
    block_dict["E"] = create_block_type_dict_e()
    block_dict["F"] = create_block_type_dict_f()
    block_dict["G"] = create_block_type_dict_g()
    block_dict["H"] = create_block_type_dict_h()
    block_dict["I"] = create_block_type_dict_i()
    block_dict["J"] = create_block_type_dict_j()
    block_dict["K"] = create_block_type_dict_k()
    block_dict["L"] = create_block_type_dict_l()
    block_dict["M"] = create_block_type_dict_m()
    block_dict["N"] = create_block_type_dict_n()
    block_dict["O"] = create_block_type_dict_o()
    block_dict["P"] = create_block_type_dict_p()
    block_dict["Q"] = create_block_type_dict_q()
    block_dict["R"] = create_block_type_dict_r()
    block_dict["S"] = create_block_type_dict_s()
    block_dict["T"] = create_block_type_dict_t()
    block_dict["U"] = create_block_type_dict_u()
    return block_dict


if __name__ == "__main__":
    block_dict = create_block_type_dict()
    for key, dic in block_dict.items():
        print("---", key, "---")
        for pos, block_list in dic.items():
            print(pos)
            print(block_list)
