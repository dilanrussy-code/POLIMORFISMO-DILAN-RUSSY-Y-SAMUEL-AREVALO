from abc import ABC, abstractmethod 
 
 
class VehiculoAutonomo(ABC): 
 
    def __init__(self, codigo, nivel_bateria): 
        self.codigo = codigo 
        self.nivel_bateria = nivel_bateria 
 
    @abstractmethod 
    def mover(self, distancia): 
        pass 
 
    @abstractmethod 
    def calcular_consumo(self, distancia): 
        pass 
 
 
class AutomovilElectrico(VehiculoAutonomo): 
 
    def __init__(self, codigo, nivel_bateria, consumo_km): 
        super().__init__(codigo, nivel_bateria) 
        self.consumo_km = consumo_km 
 
    def calcular_consumo(self, distancia): 
        return distancia * self.consumo_km 
 
    def mover(self, distancia): 
        consumo = self.calcular_consumo(distancia) 
 
        if consumo <= self.nivel_bateria: 
            self.nivel_bateria -= consumo 
            print(f"Automóvil {self.codigo}: recorrió {distancia} km") 
            print(f"Consumo: {consumo}") 
            print(f"Batería restante: {self.nivel_bateria}") 
        else: 
            print(f"Automóvil {self.codigo}: batería insuficiente") 
 
 
class Dron(VehiculoAutonomo): 
 
    def __init__(self, codigo, nivel_bateria, consumo_km, altura): 
        super().__init__(codigo, nivel_bateria) 
        self.consumo_km = consumo_km 
        self.altura = altura 
 
    def calcular_consumo(self, distancia): 
        return (distancia * self.consumo_km) + self.altura 
 
    def mover(self, distancia): 
        consumo = self.calcular_consumo(distancia) 
 
        if consumo <= self.nivel_bateria: 
            self.nivel_bateria -= consumo 
            print(f"Dron {self.codigo}: recorrió {distancia} km") 
            print(f"Consumo: {consumo}") 
            print(f"Batería restante: {self.nivel_bateria}") 
        else: 
            print(f"Dron {self.codigo}: batería insuficiente") 
 
 
class RobotTerrestre(VehiculoAutonomo): 
 
    def __init__(self, codigo, nivel_bateria, consumo_km, peso_carga): 
        super().__init__(codigo, nivel_bateria) 
        self.consumo_km = consumo_km 
        self.peso_carga = peso_carga 
 
    def calcular_consumo(self, distancia): 
        return (distancia * self.consumo_km) + self.peso_carga 
 
    def mover(self, distancia): 
        consumo = self.calcular_consumo(distancia) 
 
        if consumo <= self.nivel_bateria: 
            self.nivel_bateria -= consumo 
            print(f"Robot {self.codigo}: recorrió {distancia} km") 
            print(f"Consumo: {consumo}") 
            print(f"Batería restante: {self.nivel_bateria}") 
        else: 
            print(f"Robot {self.codigo}: batería insuficiente") 
 
vehiculos = [ 
    AutomovilElectrico("A01", 100, 2), 
    Dron("D01", 100, 3, 10), 
    RobotTerrestre("R01", 100, 2, 15) 
] 
 
for vehiculo in vehiculos: 
    vehiculo.mover(10) 
    print()  AHORA ESTE
