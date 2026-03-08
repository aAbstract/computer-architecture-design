#!/bin/bash

yosys -p "read_verilog verilog/$1/$1.v; synth -nofsm -top $1; write_json verilog/$1/$1.json" && netlistsvg verilog/$1/$1.json -o verilog/$1/$1.svg
