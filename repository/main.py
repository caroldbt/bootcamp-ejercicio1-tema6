class Vehiculo(object):
    def __init__(self, color, puerta, rueda):
        #"Constructor de Vehiculo"
        self.color = color
        self.puerta = puerta
        self.rueda = rueda
    def __str__(self):
        return "\nColor: %s\nNumero Puertas: %s\nNumero de ruedas: %s" %(str(self.color), self.puerta, self.rueda)
class Coche(Vehiculo):
    #Constructor de Coche
    def __init__(self, color, puerta, rueda, cilindrada,velocidad):
        # llamamos al constructor de Vehiculo
        Vehiculo.__init__(self, color, puerta, rueda)
        # agregamos los nuevos atributo
        self.cilindrada = cilindrada
        self.velocidad = velocidad

coche = Coche("Rojo", 4,4,100,1000)
print("Caracteristicas de un Coche:",coche,"\nCilindrada",coche.cilindrada,"\nVelocidad",coche.velocidad)

