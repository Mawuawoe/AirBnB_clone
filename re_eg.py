#!/usr/bin/python3
import re

# Search for the pattern "world" in the string "Hello, world!"
result = re.search("world", "Hello, world!")

# Check if a match was found
if result:
    print("Pattern found at position:", result)
else:
    print("Pattern not found.")
