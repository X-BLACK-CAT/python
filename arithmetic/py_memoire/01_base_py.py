temp = []
string = '24fa6ffac'
for s in string:
    a = ord(s)+5
    temp.append(chr(a))

text = ''.join(temp)
print(text)
