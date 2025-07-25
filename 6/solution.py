code_map = {
    1: "l", 2: "p", 3: "a", 4: "y", 5: "b", 6: "f", 7: "o", 8: "h", 9: "d", 10: "q", 11: "z", 12: "c", 13: "v", 14: "x",
    15: "g", 16: "i", 17: "s", 18: "e", 19: "w", 20: "u", 21: "r", 22: "j", 23: "k", 24: "t", 25: "n", 26: "m", 27: " ",
}

code = [8, 18, 1, 1, 7, 27, 5, 20, 5, 5, 3, 27, 9, 20, 5, 11, 11]

decoded_message = []
for x in code:
    decoded_x = code_map[x]
    decoded_message.append(decoded_x)

print(decoded_message)

# Slightly more advanced method:
decoded_message2 = [code_map[x] for x in code]

print(decoded_message2)