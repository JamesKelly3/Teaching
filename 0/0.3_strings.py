"""
strings are a way to represent any text you want, you can add strings together and it'll just stick one on the end of the other
you can also make substrings and "multiply" string
In python use can use either " or ' when you type a string
"""
text = "Hello, I'm a computer"
text2 = ", what's your name?"

added = text + text2
substring = text[0:5] # get the first 5 characters of the string
multiplied = substring * 5

print(f"{added=}, {substring=}, {multiplied=}")