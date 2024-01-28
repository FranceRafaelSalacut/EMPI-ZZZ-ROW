from icecream import ic #a library for easier debug

ic.disable()

i = int(input())
ic(type(i))
arr = []
ic(type(arr))

for _ in range(0, i):
    arr.append(input())


ic(arr)