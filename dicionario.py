

numeros = {
    'um': 1,
    'dois': 2,
    'tres': 3,
    'quatro': 4,
    'cinco': 5,
    'seis': 6,
    'sete': 7,
    'oito': 8,
    'nove': 9,
    'dez': 10
}

# print(dict(list(numeros.items())[:3]))


# lista_numeros = []
# for num in list(numeros.items()):
#     lista_numeros.append(num)

# print(dict(lista_numeros[:3]))


lista = dict([num for num in list(numeros.items())[:3]])

print(lista)
