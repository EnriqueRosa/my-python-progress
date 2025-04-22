# Act 1 Crea una variable llamada nombre_completo que junte tu nombre y apellido con un espacio entre ellos.

my_string = "Enrique"
my_other_string = "Rosa"
print(my_string + " " + my_other_string)

# Act 2 Crea un string con salto de línea y tabulación 

my_new_line_string = "Este es un mensaje\nen dos líneas"
print(my_new_line_string)

# Act 3 Cuenta cuántas veces aparece la letra "a" en nombre_completo.

language = "Enrique Rosa"
print(language.count("a"))

# Act 4 Verifica si tu nombre completo comienza con tu nombre.

nombre_completo = "Enrique Rosa"
nombre = "Enrique"
print(nombre_completo.startswith(nombre))

# Act 5 Convierte tu nombre completo a mayúsculas y verifica si está en mayúsculas.

nombre_completo = "Enrique Rosa"
print(str.upper(nombre_completo).isupper())

# Act 6 Invierte el nombre completo.

apellido = "Rosa"
print(nombre_completo.endswith(apellido))
