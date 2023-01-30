"""
Referência:
https://www.youtube.com/watch?v=xmMXULd0dxc&ab_channel=HashtagPrograma%C3%A7%C3%A3o
"""

preco = 1000


def calcular_imposto(preco):
    return preco * 0.30

print(calcular_imposto(preco))


calcular_imposto2 = lambda x: x * 0.30
print(calcular_imposto2(preco))


precos = [100, 500, 10, 25]
impostos = list(map(lambda x: x*0.30, precos))
print(impostos)