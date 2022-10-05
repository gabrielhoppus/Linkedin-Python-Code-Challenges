"""Complete the method/function so that it converts dash/underscore delimited words into camel casing. 
The first word within the output should be capitalized only if the original word was capitalized 
(known as Upper Camel Case, also often referred to as Pascal case).

Examples
"the-stealth-warrior" gets converted to "theStealthWarrior"
"The_Stealth_Warrior" gets converted to "TheStealthWarrior"""


def to_camel_case(text):
    for ch in ["-", "_"]:
        if ch in text:
            text = text.replace(ch, " ")

    lista = list(text.split())
    i=1

    while i < len(lista):
        lista[i] = lista[i].capitalize()
        i += 1

    return ''.join(lista)

    
