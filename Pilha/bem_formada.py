#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 09:14:12 2020

@author: julia
"""
from Stack import Stack


def main():
    testes = [
            ('(3+3)', True),
            ('[()]', True),
            ('[{()}]', True),
            ('()[]{}', True),
            ('))[]}', False),
            (')', False)
            ]
    
    for t in range(len(testes)):
        resposta = bem_formada(testes[t][0])
        print(f'bem_formada("{testes[t][0]}") : {resposta} : {testes[t][1]}')


ABRE = '([{'
FECHA = ')]}'

def bem_formada(seq):
    
    pilha = Stack()
    
    for item in seq:
        
        if item in ABRE:
            pilha.push(item)
        
        elif item in FECHA:
            
            if pilha.isEmpty():
                return False
            
            topo = pilha.pop()
            if not match(topo, item):
                return False 

    return pilha.isEmpty()

def match(abre, fecha):
    
    if abre in ABRE:
        ind = ABRE.index(abre)
    return fecha == FECHA[ind]


if __name__ == '__main__':
    main()