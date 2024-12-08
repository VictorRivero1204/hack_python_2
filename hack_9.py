"""
text: {"foo":"fookziman","bar":"barziman"} output => {"Foo":"Fooziman"}
"""

def fn_hack_9(s):
    result = {k.capitalize(): v.capitalize().replace("k", "") for k, v in s.items() if k == "foo"}
    return result

print(fn_hack_9({"foo": "fookziman", "bar": "barziman"}))
