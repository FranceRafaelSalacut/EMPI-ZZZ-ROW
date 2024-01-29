'''
HONOR CODE
I declare, upon my honor, that I did this machine problem assignment by myself using references from the lecture notes and MPs.

REPO LINK
https://github.com/FranceRafaelSalacut/EMPI-ZZZ-ROW.git
'''

from icecream import ic #a library for easier debug
ic.disable()

D_TYPE = ["int",
        "char",
        "float",
        "double",
        "void"
        ]

def check_var_declaration(tokens):
    ic()
    ic(tokens)
    
    for token in tokens:
        if "(" in token or ")" in token:
            return "INVALID VARIABLE DECLARATION"
    




def check_fun_declaration(tokens):
    ic()
    ic(tokens)

def main():
    i = int(input())
    ic(type(i))

    for _ in range(0, i):
        tokens = input().split()
        ic(tokens[0])
        result = check_var_declaration(tokens[1:]) if tokens[0] == "1" else check_fun_declaration(tokens[1:])
        print(result)

main()