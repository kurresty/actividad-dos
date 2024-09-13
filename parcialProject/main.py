#conversion de tipos de datos
#Enteros a decimal
enteros = 15
ent_a_decimal=(float(enteros))

print(ent_a_decimal)

#convertir decimal a enteros

decimal=14.87
decimal_a_entero=(int(decimal))
print(decimal_a_entero)

#convertir una cadena a entero
cadena="1088947228"
cadena_a_entero=(int(cadena))
print(cadena_a_entero)


#Multilineas de cadenas
cadena="Con este  ejemplo se prueba las multilineas de cadenas \nElectiva Profesional 1\nLuis Vejarano\nIngenieria en Sistemas"
print("cadena multilinea:")
print(cadena)
print("\n")

#función len()longitud de una cadena, con esta función se cuenta cuantos caracteres tiene la cadena "Bienvenidos a mi repositorio de Github"
contar_cadena = "Bienvenidos a mi repositorio de Github"
print(f"longitud de la cadena'{contar_cadena}': {len(contar_cadena)}")
print("\n")

#sub cadenas
n = 4
#Cuenta los primeros n caracteres de una cadena
primeros_n = contar_cadena[:n]

#Cuenta los caracteres de el medio (si la longitud es impar)
medio = contar_cadena[len(contar_cadena)//2 - 1 : len(contar_cadena)//2 + 1]

#Cuenta los últimos n caracteres
ultimos_n = contar_cadena[-n:]

print("subcadenas:")
print(f"primeros {n} caracteres: {primeros_n}")
print(f"caracteres de en medio: {medio} ")
print(f"ultimos {n} caracteres: {ultimos_n} ")
print("\n")


#Funcion Upper()
print(f"'{contar_cadena}' en mayúsculas: {contar_cadena.upper()}")

#Funcion Lower()
print(f"'{contar_cadena}' en minúsculas: {contar_cadena.lower()}")
print("\n")

# Función strip() - Elimina espacios al inicio y al final
cambios_cadena = "   Ingenieria en Sistemas    "
print(f"Cadena original: '{cambios_cadena}'")
print(f"Cadena con strip: '{cambios_cadena.strip()}'")
print("\n")

# Función replace() - Reemplaza un  texto
print(f"Reemplazar 'Sistemas' , 'Industrial': {cambios_cadena.replace('Sistemas', 'Industrial')}")
print("\n")

# Función split() - Dividide una cadena en partes
print(f"Dividir la cadena en palabras: {cambios_cadena.split()}")
print("\n")

# Formato de cadenas F-String Inserta valores de variables en la cadena de texto
nombre = "Dajhana Lopez"
edad = 24
print(f"Hola, mi nombre es {nombre} y tengo {edad} años.")


