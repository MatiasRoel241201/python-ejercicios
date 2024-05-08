class Automovil:
    ruedas = 6

    def __init__(self, color, marca, aceleracion, velocidad):
        self.color = color
        self.marca = marca
        self.aceleracion = aceleracion
        self.velocidad = velocidad

    def acelera(self):
        self.velocidad = self.velocidad + self.aceleracion

    def frena(self):
        self.velocidad = self.velocidad - self.aceleracion


""" auto = Automovil('Rojo','Marca',50, 100)
print("Cantidad de ruedas: ", auto.ruedas)
print("Aceleracion: ", auto.aceleracion)
auto.acelera()
print("Aceleracion nueva: ", auto.velocidad)

auto2 = Automovil('Rojo','Marca',50, 100)
auto2.frena()
print("Aceleracion Auto 2: ", auto2.velocidad) """

class AutomovilVolador(Automovil):
    ruedas = 6
    def __init__(self, color,marca,aceleracion,velocidad, esta_volando= True):
        super().__init__(color,marca,aceleracion,velocidad)
        self.esta_volando = esta_volando

    def vuela(self):
        self.esta_volando = True

    def aterriza(self):
        self.esta_volando = False

AutomovilVolador = AutomovilVolador("Rojo","Ford",50,50)
print(AutomovilVolador.ruedas)

