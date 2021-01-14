""" Tipos de datos con Python """

""" Datos de tipo Entero 
    Ejemplo:    
        0, 1, 2, 3, 10, 20, 15 ...    --> Enteros Positivos
        -1, -6, -56, ...              --> Enteros Negativos
"""
""" Declaración de variables, asignación y impresión por consola """
enteroPositivo = 45 
print(enteroPositivo)

cero = 0
print(cero)

enteroNegativo = -56
print(enteroNegativo)

""" Datos de tipo Flotante 
    Ejemplo:
        23.45, 12.567, 3.4, 0.1     --> Flotantes Positivos
        -45.344, -6.7, -675.23      --> Flotantes Negativos
"""

flotantePositivo = 12.5
print(flotantePositivo)

flotanteNegativo = -45.567
print(flotanteNegativo)

# Si en lugar del punto decimal se coloca una coma, lo que hace es crear tuplas de números
# Una tupla sirve para agrupar, como si fueran un único valor, varios valores que, por su 
# naturaleza, deben ir juntos.
# El tipo de dato que representa una tupla se llama tuple.
tupla = 23, -56
print(tupla)    #Output:  (23, -56)

""" Datos de tipo Complejo 
    Ejemplos:
        3+2j, -4-6j, 32+34j, ... --> Números Complejos
    
    Un número complejo esta formado por una Parte Real y la Parte Imaginaria, la parte imaginaria
    cuenta con su Unidad Imaginaria.
"""

print("***** NUMEROS COMPLEJOS *****")
z1 = 6 + 2j
print(z1)

z2 = complex(3, 7)
print(z2)

z3 = complex(-3, -6)
print(z3)

z4 = complex(4, -8)
print(z4)

z5 = complex(-5, 6)
print(z5)

""" Datos de tipo cadena (string) 
    Los datos de tipo cadena se los puede escribir entre comillas simples o dobles.
"""

print("***** Cadenas *****")
nombre = "Daniel Canaviri" 
print("Nombre : " + nombre) # El simbolo + sirve para poder concatenar cadenas

profesion = 'Ingeniero de Sistemas'
print("Profesión : " + profesion)

numero1 = "3"
numero2 = "5"
print(numero1 + numero2) # Output: 35  

""" Datos de tipo Booleano 
    Los datos de tipo booleando solo pueden tener dos valores :
        Verdadero  =  True
        Falso      =  False
"""

print("***** Booleanos *****")
valorVerdadero = True 
print(valorVerdadero)

valorFalso = False 
print(valorFalso)

""" Funcion type(variable) 
    La función type me retorna el tipo de dato que almacena una variable.
"""
print(type(valorVerdadero))      # Output: <class 'bool'>
print(type(nombre))              # Output: <class 'str'>
print(type(z3))                  # Output: <class 'complex'>
print(type(z1))                  # Output: <class 'complex'>
print(type(flotantePositivo))    # Output: <class 'float'>
print(type(enteroNegativo))      # Output: <class 'int'>
print(type(tupla))               # Output: <class 'tuple'>