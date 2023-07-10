# decored function


def decorador(registro):
    def interna(nombre):
        print("Bienvenido")
        registro(nombre)
        print("Gracias por unirte")
    return interna

@decorador
def registro (nombre):
    print(nombre) 
        

registro("Adan")