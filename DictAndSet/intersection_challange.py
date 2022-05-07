text = """Education is not the learning of facts
but the training of the mind to think

– Albert Einstein"""

prepositions = {"as", "but", "by", "down", "for", "in", "of", "on", "to", "with"}

# Add your code here.
words = [word for word in text.split()]
print(set(words))

preps_used = set(words) & prepositions
print(preps_used)
