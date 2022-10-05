""" Dada a seguinte sequência: 085, 115, 092, 123, 099, 131, 106, 139, 113...
    Identifique os números da sequência maiores que 1000 e menores que 1500. """


def conta(n):
    i1 = 30
    i2 = 23
    list = []
    while n <= 1500:
        n += i1
        if n > 1000 and n < 1500:
            list.append(n)
        n -= i2
        if n > 1000 and n < 1500:
            list.append(n)
        i1 += 1
        i2 += 1
    return len(list)    

conta(85)

