animal = "  chanCHchito feliz"
print(animal.upper())
print(animal.lower())
print(animal.strip().capitalize()) # encadenar los metodos
print(animal.title()) # cada letra de cada palabra de la frase a mayuscula
print(animal.strip()) #todos los espacios izquierdas y la derecha
print(animal.lstrip()) #todos los espacios izquierdas
print(animal.rstrip()) #todos los espacios la derecha
print(animal.find("cH")) # buscar una caracetres y devuelve indice -1 no lo encontre
print(animal.replace("nCH", "j")) # reemplaza el caracter
print("nCH" in animal) # buscar si se encuentra boolena
print("nCH" not in animal) # buscar no se encuentra boolena
# metodo es una funcion que se encuentra dentro de un objeto