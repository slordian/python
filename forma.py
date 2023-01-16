class Forma():
    def __init__(self, lado1, lado2):
        """Construtor"""
        self.lado1 = lado1
        self.lado2 = lado2
    
    def calc_area(self):
        """Calcula a área da figura que dá nome à classe"""
        return self.lado1 * self.lado2
    
    def __str__(self):
        """Modifica o que vai ser impresso com print"""
        return f'A área do {str(self.__class__.__name__).lower()} é de {self.calc_area()}.' 
    
class Retangulo(Forma):
    pass

class Quadrado(Retangulo):
    def __init__(lado):
        """Igual a Retangulo, mas passa o argumento lado duas vezes para a função __init__ do Retangulo, pois todos os seus lados são iguais"""
        super().__init__(lado, lado)

# Tem algum problema com a chamada de calc_area do triangulo, resolve issaí        
class Triangulo(Retangulo):
    def __init__(self, base, altura):
        """Igual o do Retangulo mudando apenas o nome dos lados, pois, no caso do Triangulo, os lados tem nomes diferentes"""
        super().__init__(base, altura)
    
    def calc_area():
          return super().calc_area()
    
breakpoint() 