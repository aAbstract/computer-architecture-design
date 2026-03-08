#!/bin/bash

iverilog -g2005 -o sim test_comp.v tb_test_comp.v && ./sim
