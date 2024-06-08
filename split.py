#!/usr/bin/python3
from shlex import split

# Input string to be split into tokens
input_string = "command arg1 'arg2 with spaces' -option"

# Split the input string into tokens
tokens = split(input_string)

# Print the list of tokens
print("Tokens:", tokens)
print([i.strip( ) for i in split(input_string)])