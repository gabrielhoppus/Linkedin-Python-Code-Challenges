"""Write a function that takes in a string of one or more words, and returns the same string, but with all five or more letter words reversed 
(Just like the name of this Kata). Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.

Examples:

spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw" 
spinWords( "This is a test") => returns "This is a test" 
spinWords( "This is another test" )=> returns "This is rehtona test" """


def spin_words(sentence):
    lista = list(sentence.split())
    reversal = ""
    for i in range(len(lista)):
        if len(lista[i]) >= 5:
            reversal = ''.join(reversed(lista[i]))
            lista[i] = reversal

    return ' '.join(lista)

print(spin_words("Subiu Desceu Caiu Morreu"))