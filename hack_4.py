"""
generic script

text: "fooziman" output => "oozima" 
text: "barziman" output => "arzima" 
text: "qux" output => "qux" 
"""


def fn_hack_4(s):
    if len(s) > 3:
        result = s[1:]
        if len(result) > 5:
            result = result[:-1]
    else:
        result = s
    return result

print(fn_hack_4("fooziman"))  
print(fn_hack_4("barziman"))  
print(fn_hack_4("qux")) 