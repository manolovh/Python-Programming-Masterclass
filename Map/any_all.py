entries = [1, 2, 3, 4, 5]

print(f"all: {all(entries)}")
print(f"any: {any(entries)}")

print("Iterable with a 'False' value")
entries_with_zero = [1, 2, 0, 4, 5]
print(f"all: {all(entries_with_zero)}")
print(f"any: {any(entries_with_zero)}")

print('=' * 20)
name = 'Harry'
if name:
    print(f"Hello {name}")  # Returns if `name` is True
else:
    print("Hello, person with no name")  # Returns if `name` is False
