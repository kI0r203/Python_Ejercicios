frase = input("Dime una frase y te calculo cuanto tiempo tardaras en decirlo: ")
cantidad_palabras = len(frase.split(' '))
tiempo_decir_frase = cantidad_palabras / 2

print(f'Tardarias {tiempo_decir_frase}s en decir la frase')
print(f'Dijiste {cantidad_palabras} palabras')

if tiempo_decir_frase >= 60:
    print("Para flaco tampoco te pedi un testamento")

tiempo_dalto_decir_frase = tiempo_decir_frase - (tiempo_decir_frase *30 /100)

print(f'Dalto diria la frase en {tiempo_dalto_decir_frase}s') 