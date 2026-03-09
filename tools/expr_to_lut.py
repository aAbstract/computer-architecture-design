import re
import math
import argparse

from tools.utils import *


def extract_symbols(expr: str) -> list[str]:
    return re.findall(r'[A-Za-z_]+', expr)


def exhst_bit_seq(num_bits: int) -> list[str]:
    out: list[str] = []
    max_n = int(math.pow(2, num_bits))
    for i in range(max_n):
        out.append(bin(i)[2:].zfill(num_bits))
    return out


def boolean_eval(expr: str, syms_list: list[str], syms_vals: str) -> int:
    if len(syms_list) != len(syms_vals):
        return

    es_mem: dict[str, int] = {s: int(syms_vals[idx]) for idx, s in enumerate(syms_list)}
    return eval(expr, es_mem)


def expr_solve(expr: str) -> list[tuple[str, int]]:
    syms = extract_symbols(expr)
    in_bin_seq_list = exhst_bit_seq(len(syms))
    return [(seq, boolean_eval(expr, syms, seq)) for seq in in_bin_seq_list]


def disp_expr_sol(syms_list: list[str], sol: list[tuple[str, int]]):
    print("\t".join(syms_list) + '\tOut')
    for seq, res in sol:
        print("\t".join(list(seq)) + f"\t{res}")


if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser(description='Converts Boolean Expression to Look up Table.', epilog='Example: expr_to_lut -e "A ^ B ^ C_in" -d')
    arg_parser.add_argument('--expr', '-e', help='Boolean Expression', required=True)
    arg_parser.add_argument('--cfmt', '-f', choices=['M', 'V'], help='LUT Code Format: M -> MatLab, V -> Verilog', default='M')
    arg_parser.add_argument('--debug', '-d', help='Print Debug Results', action='store_true')

    args = arg_parser.parse_args()
    expr: str = args.expr

    sol = expr_solve(expr)

    debug: bool = args.debug
    if debug:
        disp_expr_sol(extract_symbols(expr), sol)
