'''
HONOR CODE
I declare, upon my honor, that I did this machine problem assignment by myself using references from the lecture notes and MPs.

REPO LINK
https://github.com/FranceRafaelSalacut/EMPI-ZZZ-ROW.git

This code is very dirty all over
'''

# from icecream import ic #a library for easier debug
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

# STATES FOR VAR DECLARATION
TYPE_DETECT = 0
VAR_NAME_DETECT = 1
VAR_VALUE_DETECT = 2
STATES = [TYPE_DETECT, VAR_NAME_DETECT, VAR_VALUE_DETECT]
    
        
def check_if_match(var_d_type, value, declared):

    # IF THE DATA TYPE CONVERSION FAILS WE WILL CHECK IF THE VALUE IS ALREADY A DECLARED VARIABLE OR IF THE VARIABLE IS AN ASCII CODE
    try:
        if var_d_type == "char":
            #ic(value)
            if "'" in value:
                #ic()
                value = value.replace("'","")
            #ic(value)
            #ic(len(value))
            #ic(value.isalpha())
            if len(value) != 1 and value.isalpha():
                #ic()
                return False

        if var_d_type == "int":
            #ic()
            return isinstance(int(value), int)
                
        # THERE IS NO DIFFERENCE BETWEEN FLOAT AND DOUBLE IN PYTHON
        if var_d_type == "float":
            #ic()
            return isinstance(float(value), (int, float))
                
        if var_d_type == "double":
            #ic()
            return isinstance(float(value), (int, float))
            
        #ic()
        return True
    except:

        # CHECKING IF IT VALUE ALREADY DECLARED
        #ic()
        
        passed = False

        for key,val in declared.items():
            #ic(key)
            #ic(value)
            if key == var_d_type:
                for item in val:
                    if item == value:
                        passed = True

        # CHECKING IF ITS AN ASCII VALUE
        if var_d_type == "int" and "'" in value:
            value = value.replace("'","")
            passed = isinstance(ord(value), int)
        
        return passed

def add_to_dict(dict, data_type, value):
    if data_type in dict:
        list = dict[data_type]
        list.append(value)
        dict[data_type] = list
        return dict
    
    dict[data_type] = [value]
    return dict

def valid_name(name):
    if name in D_TYPE:
        return False
    if "_" in name:
        name = name.replace("_", "")

    if not name[0].isalpha():
        return False
    
    return name.isalnum()

def check_var_declaration(word):
    #ic()
    # CHECKING IF THE TOKENS HAS A PARENTHESIS MEANING ITS A FUNCTION
    for token in word:
        if "(" in token or ")" in token:
            return IVD
    
    # CHECKING FOR THE SPACE AFTER THE TEST INDICATOR
    if word[0] == " ":
        word = word[1:]
    else:
        return IVD
    

    ##ic(word)
    temp = ""
    data_type = ""
    declared = {}
    has_comma = False
    CURRENT_STATE = TYPE_DETECT
    for i,token in enumerate(word):
        # CHECKING IF THE DATA TYPE IS CORRECT
        if CURRENT_STATE == TYPE_DETECT:
            if token == " ":
                if word[i-1] == ";" or word[i-1] == " ":
                    continue
                if temp not in D_TYPE:
                    return IVD
                data_type = temp
                CURRENT_STATE = VAR_NAME_DETECT
                temp = ""
                continue
            temp = temp + token
        
        # CHECKING IF VAR NAME IS CORRECT
        elif CURRENT_STATE == VAR_NAME_DETECT:
            if token == "=":
                if len(temp) != 0:
                    if not valid_name(temp):
                        return IVD
                    #ic("VALID")
                CURRENT_STATE = VAR_VALUE_DETECT
                declared = add_to_dict(declared, data_type, temp)
                temp = ""
                continue

            if token == ",":
                has_comma = True
                if not valid_name(temp):
                    return IVD
                declared = add_to_dict(declared, data_type, temp)
                #ic("VALID")
                temp = ""
                continue

            if token == " ":
                #ic(word[i-1])
                #ic(word[i+1])
                if word[i-1] != ",":
                    #ic()
                    if word[i+1] != " " and word[i+1] != ";" and word[i+1] != "=":
                        if has_comma:
                            has_comma = False
                        else:
                            return IVD

                token = ""
            
            if token == ";":
                if len(temp) != 0:
                    if not valid_name(temp):
                        return IVD
                CURRENT_STATE = TYPE_DETECT
                declared = add_to_dict(declared, data_type, temp)
                temp = ""
                continue

            temp = temp + token
        
        # CHECKINBG IF VAR VALUE IS CORRECT
        elif CURRENT_STATE ==  VAR_VALUE_DETECT:
            if token == " ":
                token = ""
            if token == ",":
                if not check_if_match(data_type, temp, declared):
                    return IVD
                CURRENT_STATE = VAR_NAME_DETECT
                temp = ""
                continue
            if token == ";":
                if not check_if_match(data_type, temp, declared):
                    return IVD
                CURRENT_STATE = TYPE_DETECT
                temp = ""
                continue
            temp = temp + token
        
        #ic(temp)
        #ic(CURRENT_STATE)
    #ic()
    return VVD


def check_fun_declaration(tokens):
    pass
    ##ic()
    ##ic(tokens)

def main():
    i = int(input())
    ##ic(type(i))

    for _ in range(0, i):
        word = input()
        ##ic(word[0])
        result = check_var_declaration(word[1:]) if word[0] == "1" else check_fun_declaration(word[1:])
        #ic(result)
        print(result)

main()