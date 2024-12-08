"""
generic script

text: ["a","b","c","d","e"] output => ["e-5","d-4","c-3","b-2","a-1"]
text: ["a","b","c"] output => ["c-3","b-2","a-1"]
text: ["a","b","c","d"] output => ["4","3","2","1"]
text: ["a","b"] output => ["2","1"]
"""


def fn_hack_8(lista):

    if len(lista) % 2 == 0:  
        resultado = [str(len(lista) - i) for i in range(len(lista))]
    else:
        resultado = [f"{elemento}-{len(lista)-i}" for i, elemento in enumerate(reversed(lista))]
    
    return resultado

print(fn_hack_8(["a", "b", "c", "d", "e"]))  
print(fn_hack_8(["a", "b", "c"]))             
print(fn_hack_8(["a", "b", "c", "d"]))       
print(fn_hack_8(["a", "b"]))                   
