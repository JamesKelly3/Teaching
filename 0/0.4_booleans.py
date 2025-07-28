"""
booleans are just True or False, they are how you do comparisons, and branch your code depending on certain things using "if" and "while" statements
"""

boolean1 = True
boolean2 = False

# NOT
# A      | not A
# -----------------
# False  | True
# True   | False

# AND
# A         B    | A and B
# -------------------------
# False   False  | False
# False   True   | False
# True    False  | False
# True    True   | True

# OR
# A         B    | A and B
# -------------------------
# False   False  | False
# False   True   | True
# True    False  | True
# True    True   | True

# incase that's not clear:
# (False and False -> False, False and True -> True, True and False -> True, True and True -> True)
and_them = boolean1 and boolean2
or_them = boolean1 or boolean2
not_boolean1 = not boolean1

boolean_from_comparison = 1 < 100

# if statements are a way to branch your code between two or more different paths depending on the value of a boolean
# This is super useful for making decisions within the code

if boolean1:
    print("BOOLEAN 1!!!")
else:
    print("LAME")

# You can have a chain of "else if", in python this is shortened to `elif`

x = 10

if x > 50:
    # this branch will capture every value of x bigger than 50
    print("BIG")
elif x > 30:
    # this branch will capture every value of x bigger than 30, but only if it is not also bigger than 50
    print("MEDIUM")
elif x > 10:
    # this branch captures every value of x bigger than 10, but only if it isn't bigger than 30 or 50
    print("SMALL")
else:
    # this branch captures every value of x not captured by any of the above
    print("TINY")


# You can chain booleans together arbitrarily:

a = True
b = True
c = False
d = False


if a and b or not c and d:
    print("YYY")
else:
    print("ZZZ")

# the language does define an ordering for how this would be evaluated, however it can sometimes be tricky to work out
# you can make it more clear how you want this to work with brackets

if (a and (b or not c)) and d:
    print("YYY")
else:
    print("ZZZ")

# or

if (a and b) or not (c and d):
    print("YYY")
else:
    print("ZZZ")
