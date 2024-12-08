"""
generic script

["1","-"] => type string
["0"] => type string

text: ["a","b","c","d","e"] output => ["1","-","3","-","5"]
text: [] output => ["0"] 
"""


def fn_hack_6(s):
    if not s :
        return ["0"]
    
    result = []
    for n in range(len(s)):
        if n % 2 == 0:
            result.append(str(n+1))
            if n + 2 < len(s):
                result.append("-")
    return result

print(fn_hack_6(["a", "b", "c", "d", "e"]))  
print(fn_hack_6([]))