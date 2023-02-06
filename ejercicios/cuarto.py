def numeros_primos(num):
    primos = list()
    for i in range(3,num+1):
        if es_primo(i): primos.append(i)
    return primos
    
def es_primo(num):
    for i in range(2,num):
        if num%i == 0: return False
    return True

resultado = numeros_primos(100)
print(resultado[22])