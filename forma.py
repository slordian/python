from math import pi, sqrt

class Forma():
    def __init__(self, lado1, lado2):
        """Construtor"""
        self.lado1 = lado1
        self.lado2 = lado2
    
    def calc_area(self):
        """Calcula a área da figura que dá nome à classe"""
        return float(self.lado1 * self.lado2)
    
    def __str__(self):
        """Modifica o que vai ser impresso"""
        return f'A área do {str(self.__class__.__name__).lower()} é de {self.calc_area():.3f}.' 
    
class Retangulo(Forma):
    pass

class Quadrado(Retangulo):
    def __init__(self, lado):
        """Igual a Retangulo, mas passa o argumento lado duas vezes para a função __init__ do Retangulo, pois todos os seus lados são iguais"""
        super().__init__(lado, lado)
      
class Triangulo(Retangulo):
    def __init__(self, base, altura):
        """Igual o do Retangulo mudando apenas o nome dos lados, pois, 
        no caso do Triangulo, os lados tem nomes diferentes"""
        super().__init__(base, altura)
    
    def calc_area(self):
          return super().calc_area() / 2
      
class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio

    def calc_area(self):
        return pi * self.raio ** 2
    
class Hexagono(Quadrado):
    def calc_area(self):
        area = (3 * (self.lado1 ** 2) * sqrt(3)) / 2
        return area

class Programa():
    def __init__(self):
        pass
    
    # implementa isso aí depois kkkkk
    def run():
        while True:
            pass
    
    
    
def main():
    run = Programa()
    run.run()

    
if __name__ == '__main__':
    main()
    