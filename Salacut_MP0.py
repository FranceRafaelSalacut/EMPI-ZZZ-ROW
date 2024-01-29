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


def check_if_match(var_d_type, value):
    if var_d_type == "char":
        ic()
        if len(value != 1):
            ic()
            return False
        
    if var_d_type == "int":
        ic()
        if not isinstance(value, int):
            ic()
            return False

    # THERE IS NO DIFFERENCE BETWEEN FLOAT AND DOUBLE IN PYTHON
    if var_d_type == "float":
        ic()
        if not isinstance(value, float):
            ic()
            return False
            
    if var_d_type == "double":
        ic()
        if not isinstance(value, float):
            ic()
            return False
        
    return True
        

def check_var_declaration(tokens):
    # CHECKING IF THE TOKENS HAS A PARENTHESIS MEANING ITS A FUNCTION
    if len(tokens) == 0:
        return

    for token in tokens:
        if "(" in token or ")" in token:
            return IVD
    
    if tokens[0] not in D_TYPE:
        return IVD
    
    #  VARIABLE DATA TYPE
    var_d_type = tokens[0]

    tokens.pop(0)

    while(True):
        # https://stackoverflow.com/questions/57062794/is-there-a-way-to-check-if-a-string-contains-special-characters
        ic(tokens)
        token = tokens[0]
        if token.count(",") > 0:
            # print(True)
            fragments = token.split(",")
            fragments.remove("")
            ic(fragments)
            for part in fragments:
                if not part.isalnum():
                    return IVD
            tokens.pop(0)
        else:
            if token == "=":
                tokens.pop(0)
                break
            elif token.count(";") > 1:
                break
            else:
                if not token.isalnum():
                    return IVD
                else:
                    tokens.pop(0)
                    break

    token = tokens[0]
    if token.count(";") > 1:
        fragments = token.split(";")
        fragments.remove("")
        if not check_if_match(var_d_type, fragments):
            return IVD
        token.pop(0)
        return check_var_declaration(tokens)
    return VVD
            

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