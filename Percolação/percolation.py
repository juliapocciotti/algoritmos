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
            for x in range(m):
                if self.grid[i, x] == BLOCKED:
                    rede += '|   ' 
                elif self.grid[i, x] == OPEN:
                    rede += '| o '
                elif self.grid[i, x] == FULL:
                    rede += '| x '
            
            rede += '|'
            rede += '\n'
        
        final = '+' + '---+' * (m) 
        rede += final 
        
        rede += f'\ngrade de dimensão: {n}x{m}'
        rede += f'\nno. sítios abertos: {self.no_open()}'
        rede += f'\npercolou: {self.percolates()}'
        return rede 

    def is_open(self, lin, col):
        if self.grid[lin, col] == FULL:
            return True
        elif self.grid[lin, col] == OPEN:
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
                if j == OPEN or j == FULL:
                    n_open.append(j)
        return len(n_open)
    
    def get_grid(self):
        return self.grid.copy()
    
    def open(self, lin, col):        

        if self.grid[lin,col] == BLOCKED:
           self.grid[lin, col] = OPEN
    
        if lin == 0:
            self.grid[lin, col] = FULL
            return None 
        
        visitas = np.full(self.shape, 0)
        
        q = Fila()
        
        n, m  = self.shape
        
        q.insere((lin, col))
        repetidor = 0 
        while not q.vazia():
            vizinhos = [(lin-1, col),
                        (lin+1, col),
                        (lin, col+1),
                        (lin, col-1)]
            
            for v in range(len(vizinhos)):
                linha, coluna = vizinhos[v]
                
                if  0 <= linha < n and  0 <= coluna < m:
                
                    if self.grid[linha, coluna] != BLOCKED:
                
                        if visitas[linha,coluna] != 1:
                            q.insere((linha,coluna))
                            visitas[linha,coluna] = 1
            
            i, j = q.remove()
            if self.grid[i, j] == FULL:
                self.grid[lin, col] = FULL
            
            if self.grid[i, j] == OPEN and self.grid[lin, col] == OPEN:
                if repetidor < 2:
                    q.insere((i,j))
                    repetidor += 1
            
            while self.grid[i,j] == OPEN and self.grid[lin,col] == FULL:
                
                self.grid[i, j] = FULL  
                lin, col = i, j
                vizinhos = [(lin-1, col),
                            (lin+1, col),
                            (lin, col+1),
                            (lin, col-1)]

                for v in range(len(vizinhos)):
                    linha, coluna = vizinhos[v]        
                    
                    if  0 <= linha < n and  0 <= coluna < m:
                    
                        if self.grid[linha, coluna] != BLOCKED:
                            
                            q.insere((linha,coluna))
                            visitas[linha,coluna] = 1
                
                
    def percolates(self):
        full = []
       
        n = len(self.grid)-1
        for i in self.grid[n]:
            if i == FULL:
                full.append(i)              

        if len(full)>=1:
            return True
        
        return False 

class Fila:
    def __init__(self):
        self.itens = []

    def __str__(self):
        return str(self.itens)
        
    def vazia(self):
        return self.itens == []

    def insere(self, item):
        self.itens.append(item) 

    def remove(self):
        return self.itens.pop(0) 

    def __len__(self):
        return len(self.itens)
           