def remove_exclamation_marks(s):
    return ''.join([x for x in s if x != '!'])

print(remove_exclamation_marks("Hello World!!!"))