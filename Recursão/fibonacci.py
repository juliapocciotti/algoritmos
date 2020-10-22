def main():
    print(f"fibonacci(0)  = {fibonacciRM(0)}")
    print(f"fibonacci(10) = {fibonacciRM(10)}")
    print(f"fibonacci(20) = {fibonacciRM(20)}") 
    print(f"fibonacci(30) = {fibonacciRM(30)}") 
    print(f"fibonacci(31) = {fibonacciRM(31)}")
    print(f"fibonacci(32) = {fibonacciRM(32)}") 
    print(f"fibonacci(33) = {fibonacciRM(33)}") 
    print(f"fibonacci(34) = {fibonacciRM(34)}") 
    print(f"fibonacci(35) = {fibonacciRM(35)}") 
    print(f"fibonacci(36) = {fibonacciRM(36)}") 
    print(f"fibonacci(37) = {fibonacciRM(37)}") 
    print(f"fibonacci(38) = {fibonacciRM(38)}") 
    print("Chega!")
    
#------------------------------------------------    
# VERSÃO ITERATIVA
def fibonacciI(n):
    if n == 0: return 0
    if n == 1: return 1
    anterior = 0
    atual = 1
    for i in range(1, n):
        prox = atual + anterior
        anterior = atual
        atual = prox
    return atual 

# VERSÃO RECURSIVA
def fibonacciR(n):
    '''(int) -> int
    RECEBE um inteiro não negativo n.
    RETORNA o n-ésimo número de Fibonacci.
    '''
    #base
    if n < 2: return n 
    #reduza
    n_1 = fibonacciR(n-1)
    n_2 = fibonacciR(n-2)
    #resolva
    return n_1 + n_2

# VERSÃO RECURSIVA COM MEMÓRIA
def fibonacciRM(n):
    '''(int) -> int
    RECEBE um inteiro não negativo n.
    RETORNA o n-ésimo número de Fibonacci.
    '''
    if n < 2: return n 
    # cache
    cache = [-1]*(n+1)
    #base
    cache[0] = 0
    cache[1] = 1
    #resolve
    return fibonacciRC(n, cache)

def fibonacciRC(n, cache):
    #base    
    if cache[n] != -1: return cache[n]
    
    #reduza
    cache[n-1] = fibonacciRC(n-1, cache)
    cache[n-2] = fibonacciRC(n-2, cache)
    
    #resolva
    cache[n] = cache[n-1] + cache[n-2]
    return cache[n]    

    
if __name__ == "__main__":
    main()