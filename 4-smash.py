def smash(words):
    return ' '.join(word for word in words)

print(smash(["hello", "world"]))
print(smash(["hello", "amazing", "world"]))
print(smash(["this", "is", "a", "really", "long", "sentence"]))