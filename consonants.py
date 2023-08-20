import string

all_alphabets = string.ascii_lowercase

# for letters in all_alphabets:
#     for numbers in range(26):
#         letters=numbers
#         print(sum(letters))

# dict(for letters in all_alphabets = for i in range(26))

alphabets = [letters for letters in all_alphabets]
numbers = [num for num in range(1,27)]
print(alphabets)
lettersDic = dict(letters for letters in all_alphabets:num for num in range(1,27))
print(lettersDic)