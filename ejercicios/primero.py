otros_Coursos_min = 2.5
otros_Coursos_max = 7
otros_Coursos_promedio = 4
dalto_curso = 1.5

diferencia_con_min = round(100 - dalto_curso * 100 / otros_Coursos_min,2)
diferencia_con_max = round(100 - dalto_curso * 100 / otros_Coursos_max,2)
diferencia_con_promedio = round(100 - dalto_curso * 100 / otros_Coursos_promedio,2)

print(f'La diferenca en porcentaje con el curso que dura menos es: {diferencia_con_min}%')
print(f'La diferenca en porcentaje con el curso que dura mas es: {diferencia_con_max}%')
print(f'La diferenca en porcentaje con el promedio de cursos es: {diferencia_con_promedio}%')

crudo_promedio = 5
crudo_dalto = 3.5

tiempo_vacio_promedio = round(100 - otros_Coursos_promedio * 100/crudo_promedio,2)
tiempo_vacio_dalto = round(100 - dalto_curso * 100/crudo_dalto,2)

print(f'Un curso promedio elimina el {tiempo_vacio_promedio}% de tiempo vacio')
print(f'Este curso elimino el {tiempo_vacio_dalto}% de tiempo vacio')

print(f'Ver 10 horas de este cursos equivale a ver {round(otros_Coursos_promedio / dalto_curso * 10,1)} horas de otros cursos')
print(f'Ver 10 horas de otros cursos equivale a ver {round(dalto_curso / otros_Coursos_promedio * 10,1)} horas de este curso')
