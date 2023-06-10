from clase1 import Vehiculo, Automovil


instancias =[]

n = int(input("Cuantos Vehículos desea insertar: "))

for i in range(n):
    print(f"Datos del automóvil {i+1}")
    marca = input("Inserte la marca del automóvil: ")
    modelo = input("Inserte el modelo: ")
    nruedas = int(input("Inserte el número de ruedas "))
    velocidad = int(input("Inserte la velocidad en km/h: "))
    cilindraje = int(input("Inserte el cilindraje en cc: "))
    print("")
    auto = Automovil(marca, modelo, nruedas, velocidad, cilindraje)
    instancias.append(auto)

print("Imprimiendo por pantalla los Vehículos:")



for index,item in enumerate(instancias):
    print(f"Datos del automóvil {index + 1} : Marca {item.marca}, Modelo {item.modelo}, {item.nruedas} ruedas, {item.velocidad} km/h, {item.cilindraje} cc")