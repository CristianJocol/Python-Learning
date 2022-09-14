# Objetivo: Concatenar cadenas de caracteres
# Aprende a programa con ____________.

#Como yo lo realizaría: 

# print('ingresa el nombre de tu organización: ')
# organizacion = input()

# print('Aprende a programar con ' + organizacion + '.')

#Otras alternativas: 

# print('ingresa el nombre de tu organización: ')
# organizacion = input()
# print('Aprende a programar con {}'.format(organizacion))

#Separador --> Otra alternativa f-string form

# print('ingresa el nombre de tu organización: ')
# organizacion = input()
# print(f"Aprende a programar con {organizacion}")

#Juego palabras locas --> "Ahorcado" 

#Paso 1: Guardar la oración que el usuario ingrese: 

adj = input("Adjetivo: ")
verb = input("Verbo: ")
sus = input("Sustantivo: ")

madlib = f"Programar es super {adj} me llena de felicidad {verb}! aprende Python y alcanza tus {sus}!!!"
print(madlib)