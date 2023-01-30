""""
Referencia: 
https://www.hashtagtreinamentos.com/list-comprehension-python?gclid=CjwKCAiAoL6eBhA3EiwAXDom5jvvHjgCqkC1AgYI5fHAFCadhAEEELt4yFKmtgur7KeTGETffTJlhhoCm8YQAvD_BwE
"""

lista_precos = [500, 1500, 2000, 100, 25]


#  Caso 1: Multiplicando os valores da lista por 2
def forma_convencional() -> list:
    nova_lista_precos = []
    for preco in lista_precos:
        nova_lista_precos.append(preco * 2)
    return nova_lista_precos


def list_comprenhension() -> list:
    nova_lista_precos2 = [preco * 2 for preco in lista_precos]
    return nova_lista_precos2


# Caso: Precos aicma de $ 1.000 calcular imposto de 50% sobre o valor total
def forma_convencional1() -> list:
    imposto = []
    for preco in lista_precos:
        if preco > 1000:
            imposto.append(preco * 0.50)
    return imposto


def list_comprehension1() -> list:
    imposto2 = [preco * 0.50 for preco in lista_precos if preco > 1000]
    return imposto2


lista = list_comprehension1()
print(lista)
