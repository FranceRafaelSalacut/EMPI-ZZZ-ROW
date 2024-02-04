'''
HONOR CODE
I declare, upon my honor, that I did this machine problem assignment by myself using references from the lecture notes and MPs.

REPO LINK
https://github.com/FranceRafaelSalacut/EMPI-ZZZ-ROW.git
'''

from icecream import ic #a library for easier debug
# ic.disable()

# DATA TYPE
D_TYPE = ["int",
        "char",
        "float",
        "double",
        "void"
        ]

# RESULTS
IVD = "INVALID VARIABLE DECLARATION"
VVD = "VALID VARIABLE DECLARATION"
IFD = "INVALID FUNCTION DECLERATION"
VFD = "VALID FUNCTION DECLARATION"

    
        

def check_var_declaration(word):
    # CHECKING IF THE TOKENS HAS A PARENTHESIS MEANING ITS A FUNCTION
    if len(word) == 0:
        return
    
    ic(word)
    for token in word:
        ic(token)
            

def check_fun_declaration(tokens):
    ic()
    ic(tokens)

def main():
    i = int(input())
    ic(type(i))

    for _ in range(0, i):
        word = input()
        ic(word[0])
        result = check_var_declaration(word[1:]) if word[0] == "1" else check_fun_declaration(word[1:])
        print(result)

main()