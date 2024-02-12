
check = "void voids(void); int nextFunction(int);"
print(check[20])



elif PARAM_STATE == FUN_PARAMETER_VARNAME_DETECT: 
                #ic()
                if token == ",": 
                    #ic()
                    if not valid_name(temp):
                        return IFD
                    if check_dict(declared, temp):
                        declared = add_to_dict(declared, data_type, temp)
                    else:
                        return IFD
                    temp = ""
                    PARAM_STATE = FUN_PARAMETER_TYPE_DETECT
                    continue
                
                #ic()
                if token == " ":
                    if word[i+1] != " " and word[i+1] != ",":
                        return IFD
                    token = ""
                    
                temp = temp + token