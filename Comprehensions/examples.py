text = 'what have the romans ever done for us'

capitals = [char.upper() for char in text]

print(*capitals, sep='')

words = [word.upper() for word in text.split(' ')]
print(words)
# print(*words)
