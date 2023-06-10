class Vehiculo():
    def __init__(self, marca, modelo, nruedas, velocidad, cilindraje):
        self.marca = marca
        self.modelo = modelo
        self.nruedas = nruedas
        self.velocidad = velocidad
        self.cilindraje = cilindraje

    def __str__(self):
        return f"Marca {self.marca}, Modelo {self.modelo}, {self.nruedas} ruedas, {self.velocidad} Km/h, {self.cilindraje} cc"


class Automovil(Vehiculo):
    pass


    
class Particular(Automovil):
    def __init__(self, marca, modelo, nruedas, velocidad, cilindraje, npuestos):
        super().__init__(marca, modelo, nruedas, velocidad, cilindraje)
        self.npuestos = npuestos

    def __str__(self):
        return f"Marca {self.marca}, Modelo {self.modelo}, {self.nruedas} ruedas, {self.velocidad} Km/h, {self.cilindraje} cc, npuestos: {self.npuestos}"



class Carga(Automovil):
    def __init__(self, marca, modelo, nruedas, velocidad, cilindraje, carga):
        super().__init__(marca, modelo, nruedas, velocidad, cilindraje)
        self.carga = carga

    def __str__(self):
        return f"Marca {self.marca}, Modelo {self.modelo}, {self.nruedas} ruedas, {self.velocidad} Km/h, {self.cilindraje} cc, Carga: {self.carga} Kg"



class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, nruedas, tipo):
        super().__init__(marca, modelo, nruedas, 0, 0)
        self.tipo = tipo

    def __str__(self):
        return f"Marca {self.marca}, Modelo {self.modelo}, {self.nruedas} ruedas, Tipo: {self.tipo}"


class Motocicleta(Bicicleta):
    def __init__(self, marca, modelo, nruedas, tipo, motor, cuadro, nradios):
        super().__init__(marca, modelo, nruedas, tipo)
        self.motor = motor
        self.cuadro = cuadro
        self.nradios = nradios

    def __str__(self):
        return f"Marca {self.marca}, Modelo {self.modelo}, {self.nruedas} ruedas, Tipo: {self.tipo}, Motor: {self.motor}, Cuadro: {self.cuadro}, nradios: {self.nradios}"
    
