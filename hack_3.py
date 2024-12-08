"""
generic script

text: "fooziman" output => "F00z¡m@N" 
text: "barziman" output => "B@rz¡m@N" 
text: "3q" output => "3Q" 
text: "qu" output => "Qv" 
text: "qux" output => "QvX" 
"""

replacement = {
    'a' : '@',
    'e' : '3',
    'i' : '¡',
    'o' : '0',
    'u' : 'v',
    'z' : 'z',
    'f' : 'F',
    'b' : 'B',
    'q' : 'Q',
    'n' : 'N',
    'x' : 'X',
}

def fn_hack_3(s):
    result = ""
    for char in s:
        if char.lower() in replacement:
            if char.isupper():
                result += replacement[char.lower()].upper()
            else:
                result += replacement[char.lower()]
        elif char.isalpha():
            result += char.lower() 
        else:
            result += char
    return result

print(fn_hack_3("fooziman"))  
print(fn_hack_3("barziman"))  
print(fn_hack_3("3q"))        
print(fn_hack_3("qu"))        
print(fn_hack_3("qux")) 