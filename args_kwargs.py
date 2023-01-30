"""
Referencia:
https://www.youtube.com/watch?v=RcqHJ_l8GVA&ab_channel=HashtagPrograma%C3%A7%C3%A3o
"""


def calcular_imposto(valor) -> float:
    ir = valor * 0.275
    iss = valor * 0.05
    csll = valor * 0.375
    pis = valor * 0.03

    return ir + iss + csll + pis


def forma_args(valor, *args):
    total_impostos = 0
    for item in args:
        total_impostos += valor * item
    return total_impostos


def forma_kwargs(valor, **kwargs):
    total_imposto = 0
    if 'perc_ir' in kwargs.keys():
        total_imposto += valor * kwargs['perc_ir']
    # for item in kwargs.values():
    #     total_imposto += valor * item
    return total_imposto

# print(calcular_imposto(1000))
# print(forma_args(1000, 0.275, 0.05, 0.375, 0.03))
# forma_enumerate(1000, 0.275, 0.03, 0.375)

