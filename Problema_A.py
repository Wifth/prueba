class Persona:
    def __init__(self, dni=0, nombre=""):
        self.nombre = nombre
        self.dni = dni
    
    def __str__(self):
        return (f"DNI: {self.dni} | {self.nombre}")

lista = []
opc = 0
while opc != 9:
    print ("----------------------")
    print ("1. Registrar Persona")
    print ("2. Mostrar Lista")
    print ("3. Remover Persona")
    print ("4. Salir")
    print ("----------------------")
    op = int(input("Ingrese opción: "))
    if op == 1:
        dni = input("Ingrese DNI: ")
        nombre = input("Ingrese Nombre: ")
        nuevo = Persona(dni, nombre)
        lista.append(nuevo)

    elif op == 2:
        for p in lista:
            print(p)

    elif op == 3:
        buscarDNI = input("Ingrese DNI a borrar: ")
        for idx, p in enumerate(lista): # idx para el Indice
            if p.dni == buscarDNI:
                del lista[idx]
                break
    elif op == 4:
        break