def solve(word):
    consonant_values = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'f': 6, 'g': 7, 'h': 8, 'j': 10, 'k': 11, 'l': 12, 'm': 13,
                        'n': 14, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}
    
    maximum_value = 0
    current_value = 0
    
    for letter in word:
        if letter in consonant_values:
            current_value += consonant_values[letter]
            # print(current_value)
            maximum_value = max(maximum_value, current_value)
        else:
            current_value = 0
    
    return maximum_value

print(solve("strength")) 
