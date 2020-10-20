# -*- coding: utf-8 -*-
import numpy as np

#-------------------------------------------------------------------------- 
# constantes
BLOCKED = 0  # sítio bloqueado
OPEN    = 1  # sítio aberto
FULL    = 2  # sítio cheio

class Percolation:
    '''
    Representa uma grade com todos os sítios inicialmente bloqueados.
    '''
    def __init__(self, shape):
        if type(shape) == int:
            self.shape = shape, shape
            self.grid = np.full(self.shape, BLOCKED)
        elif type(shape) == tuple:
            self.grid = np.full(shape, BLOCKED)
            self.shape = shape
      
            
    def __str__(self):
        n, m = self.shape
        rede = ''
        for i in range(n):
            rede += '+'
            for x in range(m):
                rede += '---+'
            
            rede += '\n'
            rede += '|   ' * (m+1) 
            rede += '\n'
        
        final = '+' + '---+' * (m) 
        rede += final 
        
        rede += f'\ngrade de dimensão: {n}x{m}'
        return rede 











'''   
def main():
    sis1 = Percolation(1)
    
    sis2 = Percolation(2)
    
    sis3 = Percolation((3,2))
    
    sis4 = Percolation((3, 4))
    
    print(sis1.shape)
    print(sis2.shape)
    print(sis3.shape)
    print(sis4.shape)
    
    print(sis1, '\n')
    print(sis2, '\n')
    print(sis3, '\n')
    print(sis4, '\n')
    
if __name__ == '__main__':
    main()
'''