data = input()
poly = input()

d = data + '0'*(len(poly)-1)
d = list(d)
p = list(poly)

for i in range(len(data)):
    if d[i] == '1':
        for j in range(len(poly)):
            d[i+j] = str(int(d[i+j]) ^ int(p[j]))

crc = ''.join(d[-(len(poly)-1):])
print(crc)
