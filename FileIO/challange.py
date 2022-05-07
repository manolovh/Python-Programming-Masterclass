# for a in range(1, 13):
#     b = 2
#     i = a * b
#     result = (a, "times",  b, "is", i)
#     print(*result)

# with open("sample.txt", 'w') as sample_file:
#     for a in range(1, 13):
#         b = 2
#         i = a * b
#         result = (a, "times",  b, "is", i)
#         print(*result, file=sample_file)

with open("sample1.txt", 'w') as sample_file:
    for i in range(2, 13):
        for j in range(1, 13):
            print("{1:>2} times {0} is {2} ".format(i, j, i * j), file=sample_file)
        print("-" * 50, file=sample_file)
