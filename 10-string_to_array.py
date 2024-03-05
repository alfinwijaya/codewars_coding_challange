def string_to_array(s):
    arr = []
    k = 0
    for i, j in enumerate(s):
        if j == ' ':
            arr.append(s[k:i])
            k =  i + 1
        elif i == len(s) - 1:
            arr.append(s[k:i+1])

    return arr if len(arr) > 0 else ['']

print(string_to_array("Robin Singh"))
print(string_to_array("CodeWars"))
print(string_to_array("I love arrays they are my favorite"))
print(string_to_array("1 2 3"))
print(string_to_array(""))