primeira = []
segunda =  []

while True:
    e = int(input('Primeira lista: '))
    
    if e == 0:
        break
    
    primeira.append(e)

while True:
    e = int(input('Segunda lista: '))
    
    if e == 0:
        break
    segunda.append(e)

terceira = primeira[:]
terceira.extend(segunda)
x=0
while x < len(terceira):
    print("%d: %d" % (x,  terceira[x]))
    x=x+1

y = 0
x = y+1

quarta = terceira[:]
print('Terceira lista:', quarta)