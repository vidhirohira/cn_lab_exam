data = input()
FLAG = 'F'
ESC = 'E'
stuffed = FLAG

for c in data:
    if c == FLAG or c == ESC:
        stuffed += ESC + c
    else:
        stuffed += c

stuffed += FLAG
print(stuffed)
