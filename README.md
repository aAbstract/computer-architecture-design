# Computer Architecture Design

Digital Design and Computer Architecture Examples From Book "Digital Design and Computer Architecture: ARM Edition"  
Using **MATLAB/SimuLink HDL Toolkit**.

### Notes
- Set Model Settings > HDL Code Generation > Global Settings > Ports > Minimize Clock Enables

- Moore FSM Chart Settings
<p align="center">
  <img src="docs/1.png" alt="1"/>
</p>

### Expression to LUT [Tool](tools/expr_to_lut.py)
```bash
$ python tools/expr_to_lut.py -h
usage: expr_to_lut.py [-h] --expr EXPR [--cfmt {M,V}] [--debug]

Converts Boolean Expression to Look up Table.

options:
  -h, --help            show this help message and exit
  --expr EXPR, -e EXPR  Boolean Expression
  --cfmt {M,V}, -f {M,V}
                        LUT Code Format: M -> MatLab, V -> Verilog
  --debug, -d           Print Debug Results

Example: expr_to_lut -e "A ^ B ^ C_in" -d

$ python tools/expr_to_lut.py -e "A ^ B ^ C_in" -d
A       B       C_in    Out
0       0       0       0
0       0       1       1
0       1       0       1
0       1       1       0
1       0       0       1
1       0       1       0
1       1       0       0
1       1       1       1
```
