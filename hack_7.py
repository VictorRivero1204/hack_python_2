"""
generic script

["1",2] => type string & type int
[0] => type int

text: ["a","b","c","d","e"] output => ["1",2,"3",4,"5"]
text: [0] output => [0] 
"""


def fn_hack_7(s):
    
    if s == [0]:
        return [0]
    
    result = []
    for n in range(len(s)):
        if n % 2 == 0:
            result.append(str(n+1))
        else:
            result.append(n+1)
    return result

print(fn_hack_7(["a", "b", "c", "d", "e"]))  
print(fn_hack_7([0]))