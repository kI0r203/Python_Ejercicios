compañeros = list()

for i in range(4):
    compañero = input("Ingrese el nombre del compañero: ")
    edad = int(input("Ingrese la edad del compañero: "))
    compañeros.append((compañero,edad))
    
compañeros.sort(key=lambda x:x[1])

asistente = compañeros[0][0]
profesor = compañeros[-1][0]

print(f'El asistente es: {asistente} y el profesor es: {profesor}')