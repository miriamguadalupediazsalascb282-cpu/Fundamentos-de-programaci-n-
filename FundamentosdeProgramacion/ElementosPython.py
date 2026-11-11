"""
Programa para estudiar los elementos del lenguaje de programacion de Python
Mi nombre es: Guadalupe

"""
#String o charl
nombre = "Ana"    
edad = 18       #Int
estatura = 1.63   #Float o flotante
es_estudiante = True   #Boleano (verdadero o falso)

#Imprimimos la variables y su tipo
print ("Nombre:", nombre, type(nombre))
print ("Edad:", edad, type (edad))
print ("Estatura:", estatura, type (estatura))
print ("Estudiante:", es_estudiante, type (es_estudiante))

#Declaro una constante
 #Constantes
PROMEDIO_MINIMO = 6   
#introducimos datos y las guardamos en la variables materia y calificacion
#input: entrada
materia = input ("¿Que materia cursas?")  
calificacion = float(input("¿Que calificacion tienes?"))

#Hacemos operaciones basicas
suma = 8 + 2
resto = 10 % 3
potencia = 2 ** 3
mayor_de_edad = edad >= 18
aprobado = calificacion >= PROMEDIO_MINIMO and es_estudiante

print ("Suma:", suma, "|Resto:", resto, "|Potencia:", potencia)
print ("¿Mayor de edad?", mayor_de_edad)




