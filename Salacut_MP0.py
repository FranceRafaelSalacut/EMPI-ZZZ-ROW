'''
HONOR CODE
I declare, upon my honor, that I did this machine problem assignment by myself using references from the lecture notes and MPs.

REPO LINK
https://github.com/FranceRafaelSalacut/EMPI-ZZZ-ROW.git
'''

from icecream import ic #a library for easier debug

def check_var_decleration(word):
    ic()
    ic(word)

def check_fun_decleration(word):
    ic()
    ic(word)

def main():
    i = int(input())
    ic(type(i))

    for _ in range(0, i):
        div = input().split()
        ic(div[0])
        check_var_decleration(div[1:]) if div[0] == "1" else check_fun_decleration(div[1:])

main()