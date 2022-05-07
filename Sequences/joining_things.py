# flowers = [
#     "Daffodil",
#     "Evening Primrose",
#     "Hydrangea",
#     "Iris",
#     "Lavender",
#     "Sunflower",
#     "Tiger Lily",
#     "0",
# ]
# print(", ".join(flowers))
#
# separator = ", "
# output = separator.join(flowers)
# print(output)

chosen_option = input("Please select random 3 numbers, separated by a "
                      "comma:")
valid_option = chosen_option.split(",")

empty_list = []
for emp in valid_option:
    empty_list.append(int(emp))

a, b, c = empty_list
result = a + b - c

print(result)

