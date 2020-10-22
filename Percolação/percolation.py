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

    def is_open(self, lin, col):
        if self.grid[lin, col] == OPEN:
            return True
        return False 
            
    def is_full(self, lin, col):
        if self.grid[lin, col] == FULL:
            return True
        return False 

    def no_open(self):
        n_open = []
        for i in self.grid[:, :]:
            for j in i:
                if j == OPEN:
                    n_open.append(j)
        return len(n_open)
    
    def get_grid(self):
        return self.grid[:]
        
        
        
        
        
        