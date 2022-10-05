"""The goal of this exercise is to convert a string to a new string where each character in the new string is "(" 
if that character appears only once in the original string, or ")" if that character appears more than once in the original string. 
Ignore capitalization when determining if a character is a duplicate.

Examples
"din"      =>  "((("
"recede"   =>  "()()()"
"Success"  =>  ")())())"
"(( @"     =>  "))((" 
Notes
Assertion messages may be unclear about what they display in some languages. If you read "...It Should encode XXX", the "XXX" is the expected result, not the input!
"""

def duplicate_encode(word):
    list = []
    list2 = []
    i = 0
    for w in word.lower():
        list.append(w)
    for i in range(len(list)):
        count = list.count(list[i])
        if count > 1:
            list2.append(")")  
            i += 1
        else:
            list2.append("(")  
            i += 1
    return ''.join(list2)   
