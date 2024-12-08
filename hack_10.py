"""
text: [{"a":"b"},{"c","d"},{"e":"f"}] output => [{"1":"2"},{"3","4"},{"5":"6"}]
"""


def fn_hack_10(lista):
    resultado = []
    contador = 1

    for elemento in lista:
        if isinstance(elemento, dict):
            nuevo_dict = {str(contador):str(contador + 1) for _ in elemento.items()}
            resultado.append(nuevo_dict)
            contador += 2
        elif isinstance(elemento, set):
            nuevo_set = {str(contador),str(contador + 1)}
            resultado.append(nuevo_set)
            contador += 2

    return resultado

print(fn_hack_10([{"a":"b"}, {"c","d"}, {"e":"f"}]))