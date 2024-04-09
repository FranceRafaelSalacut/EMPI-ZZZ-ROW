import re

# Define a string containing special characters
string_with_special_chars = "Hello! This is a string with special characters: *&^%$#@"

# Define a regular expression pattern to match special characters
pattern = r'[^\w\s]'

# Find all special characters using the pattern
special_chars_list = re.findall(pattern, string_with_special_chars)

# Convert the list of special characters into a single string
special_chars_string = ''.join(special_chars_list)

print(special_chars_string)