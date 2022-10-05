"""Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

Examples
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !"""

def pig_it(text):
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    latin = []
    li = list(text.split(" "))
    for i in li:
        string = i
        if i in punctuations:
            latin.append(string)
        else:    
            string = string[1:] + string[0] + "ay"
            latin.append(string)

    return ' '.join(latin)
