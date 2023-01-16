class Mapa(list):
    self = []
    _x = 0
    _y = 0
    _pessoa = ''
    _chao = ''
    
    def __init__(self, largura=5, altura=5, chao='W'):
        self = [self.append([chao]*largura) for i in range(altura)]                
    
    def inicio(self, x=0, y=0, p='P'):
        self._chao = self[x][y]
        self[x][y] = p
        self._x = x
        self._y = y
        self._pessoa = p

    def show(self):
        print()
        for i in self:
            print(*i)
        print()
        
    def andar(self, direcao=str):
        self[self._x][self._y] = 'W'
        match direcao.lower():
            case 'n':
                if self._x == 0:
                    self[len(self)-1][self._y] = 'P'
                else:
                    self[self._x-1][self._y] = 'P'
            case 's':
                if self._x == len(self) - 1:
                    self[0][self._y] = 'P'
                else:
                    self[self._x+1][self._y] = 'P'
            case 'l':
                if self._y == len(self[self._x]) - 1:
                    self[self._x][0] = 'P'
                else:
                    self[self._x][self._y+1] = 'P'
            case 'o':
                if self._y == 0:
                    self[self._x][len(self[self._x])-1] = 'P'
                else:
                    self[self._x][self._y-1] = 'P'      

def main():
    print('\nOperações:\n\t1 - Iniciar o programa\n\n\t0 - Fechar o programa\n')
    operacao = int(input('O que você deseja fazer? '))
    if operacao:
        largura, altura = [int(x) for x in input('Digite a largura e a altura do mapa (larguraXaltura): ').split('x')]
        mapa = Mapa(largura, altura)