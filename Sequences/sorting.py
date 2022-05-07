pangram = "The quick brown fox jumps over the lazy dog"

letters = sorted(pangram)
print(letters)

number = [2.3, 4.5, 8.7, 9.2, 1.6]
sorted_numbers = sorted(number)
print(sorted_numbers)
print(number)

number.sort()
print(number)

missing_letter = sorted("The quick brown fox jumped over the lazy dog",
                        key=str.casefold)
print(missing_letter)

names = ["Graham",
         "John",
         "terry",
         "eric",
         "Terry",
         "michael"
        ]
names.sort(key=str.casefold)
print(names)
