L=[15,7,27,39]
p=int(input("Digite o valor de P a procurar:"))
v=int(input("Digite o valor de V a procurar:"))
x=0
y = 0

while x<len(L):
    if L[x]==p:
        break
    x+=1
    
while y<len(L):
    if L[y]==v:
        break
    y+=1
    
if L[x]==p:
	print("%d achado na posição %d" % (p,x))
else:
	print("%d não encontrado" % p)
	
if L[y]==v:
	print("%d achado na posição %d" % (v,y))
else:
	print("%d achado na posição %d" % v)