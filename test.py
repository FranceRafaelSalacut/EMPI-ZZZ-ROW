my_string = "hello world"

for i, char in enumerate(my_string):
    prev_char = my_string[i - 1] if i > 0 else None  # Previous character (or None if at the beginning)
    next_char = my_string[i + 1] if i < len(my_string) - 1 else None  # Next character (or None if at the end)
    
    print("Current:", char)
    print("Previous:", prev_char)
    print("Next:", next_char)
    print()
