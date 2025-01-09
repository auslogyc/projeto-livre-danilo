# Lâmpada da Marca A
class LampadaMarcaA:
    def ligar(self):
        print("Lâmpada da Marca A ligada")
    
    def desligar(self):
        print("Lâmpada da Marca A desligada")


# Lâmpada da Marca B
class LampadaMarcaB:
    def acender(self):
        print("Lâmpada da Marca B acesa")
    
    def apagar(self):
        print("Lâmpada da Marca B apagada")

# Interface de Lâmpada
from abc import ABC, abstractmethod

class Lampada(ABC):
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

# Adapter para Lâmpada
class AdaptadorLampada(Lampada):
    def __init__(self, lampada):
        self.lampada = lampada

    def ligar(self):
        if isinstance(self.lampada, LampadaMarcaA):
            self.lampada.ligar()
        elif isinstance(self.lampada, LampadaMarcaB):
            self.lampada.acender()

    def desligar(self):
        if isinstance(self.lampada, LampadaMarcaA):
            self.lampada.desligar()
        elif isinstance(self.lampada, LampadaMarcaB):
            self.lampada.apagar()

# Exemplos de uso
lampadaA = AdaptadorLampada(LampadaMarcaA())
lampadaB = AdaptadorLampada(LampadaMarcaB())

lampadaA.ligar()  # Saída: Lâmpada da Marca A ligada
lampadaA.desligar()  # Saída: Lâmpada da Marca A desligada
lampadaB.ligar()  # Saída: Lâmpada da Marca B acesa
lampadaB.desligar()  # Saída: Lâmpada da Marca B apagada
