text = input("Please enter your text: ")

output = []
for x in text.split():
    output.append(len(x))
print(output)


output_text = [len(x.split()) for x in text]
print(output)

output = []
for x in text.split():
    output.append((x, len(x)))
print(output)


output_text = {(x, len(x)) for x in text.split()}   # use a set so we don't get any duplicate words
print(output_text)
