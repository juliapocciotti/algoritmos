#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 09:37:12 2020

@author: julia
"""
from Stack import Stack 

PROMPT = 'Digite uma expressão posfixa:\n>>> '
OPERADORES = '+-*/'
ADD = '+'
SUB = '-'
MUL = '*'
DIV = '/'
FIM = []

def main():
    
    print("CALCULADORA POLONESA")
    print("====================\n")
    print("Tenha o cuidado de separar os termos com um espaço\n")

    exp = input(PROMPT).split()
    while exp != FIM:   
        res = valor_expressao( exp )
        print(f'Resultado: {res} = {exp}')
        exp = input(PROMPT).split()
    
    
def valor_expressao( exp ):
    ''' (lista) -> valor 
    '''
    pilha = Stack()  
    
    for item in exp:
        if item in OPERADORES: 
            if len(pilha) < 2:
                print("ERRO: faltam operandos")
                return None
            v2 = pilha.pop()
            v1 = pilha.pop()
            if item == ADD:
                valor = v1 + v2
            elif item == SUB:
                valor = v1 - v2
            elif item == MUL:
                valor = v1 * v2
            elif item == DIV:
                valor = v1 / v2
        else: # operando
            if '.' in item:
                valor = float(item)
            else:
                valor = int(item)
            
        pilha.push( valor ) 
    
    # fim dos itens
    if pilha.isEmpty():
        return 0
    elif len(pilha) > 1:
        print("ERRO: faltam operandos")
        return None
    
    resultado = pilha.pop()
    return resultado
        
main()
        
            
    
    