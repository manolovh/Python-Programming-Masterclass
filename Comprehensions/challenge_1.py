fizzbuzz_list = ["fizz buzz" if x % 15 == 0 else "fizz" if x % 3 == 0 else "buzz" if x % 5 == 0 else str(x)
                 for x in range(1, 31)]
print(fizzbuzz_list)

for buzz in fizzbuzz_list:
    print(buzz.center(12, ' '))
