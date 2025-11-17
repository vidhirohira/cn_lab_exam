data = input()
stuffed = ""
count = 0

for b in data:
    stuffed += b
    if b == '1':
        count += 1
        if count == 5:
            stuffed += '0'
            count = 0
    else:
        count = 0

print(stuffed)
