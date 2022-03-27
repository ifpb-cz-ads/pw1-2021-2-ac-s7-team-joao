T = [-10,-8,0,1,2,5,-2,-4]
soma = 0
x = 0

while x < len(T):
    soma = soma + T[x]
    x = x + 1

media = soma / len(T)

maior = max(T)
menor = min(T)

print('O maior número da lista é %d, o menor é %d e a média é %d.' %(maior, menor, media))