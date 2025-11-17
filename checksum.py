data = input().split()
s = 0

for b in data:
    s += int(b, 2)
    while s > 255:
        s = (s & 255) + 1

checksum = format(~s & 255, '08b')
print(checksum)
