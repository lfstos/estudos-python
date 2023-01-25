"""
Referencia: 
https://www.hashtagtreinamentos.com/enumerate-no-python?gclid=CjwKCAiAoL6eBhA3EiwAXDom5nu0Q61RfdOwzHIVMPIf7IJEfD3RJKNIyGbbLOA7ictHjh3vpVc8SRoCMdsQAvD_BwE
"""

vendedores = ['Marcus', 'Amanda', 'Ale', 'Carol']
vendas = [15, 20, 10, 30]


def forma_convencional():
    tamanho_lista = len(vendedores)
    for i in range(tamanho_lista):
        print(vendedores[1])
        print(vendas[i])


# Caso 2 com Enumerate
def forma_enumerate():
    for i, vendedor in enumerate(vendedores):
        print(vendedor)
        print(vendas[i])


# Caso 3: Com zip
def forma_zip():
    for vendedor, venda, in zip(vendedores, vendas):
        print(vendedor)
        print(venda)


forma_convencional()
