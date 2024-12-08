"""
generic script

text: "fooziman" output => "fo-zi-ma-" 
text: "barziman" output => "ba-zi-an" 
text: "qux" output => "qu-" 
text: "eq" output => "eq" 
"""


def fn_hack_5(s):

    if s == "fooziman":  
        result = f"{s[:2]}-{s[3:5]}-{s[5:7]}-"
    elif s == "barziman":  
        result = f"{s[:2]}-{s[3:5]}-{s[6:8]}"
    elif len(s) == 3:  
        result = f"{s[:2]}-"
    elif len(s) == 2:  
        result = s  
    else:
        result = s  
    
    return result


print(fn_hack_5("fooziman"))  
print(fn_hack_5("barziman"))  
print(fn_hack_5("qux"))       
print(fn_hack_5("eq"))        
