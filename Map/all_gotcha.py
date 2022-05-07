entries = []

if entries:
    print(f"all: {all(entries)}")
else:
    print(False)
print(f"any: {any(entries)}")

result = bool(entries) and all(entries)
print(result)