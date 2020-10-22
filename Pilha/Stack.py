#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 08:55:39 2020

@author: julia
"""

class Stack:
    def __init__(self):
        self.itens = []
        
    def isEmpty(self):
        return len(self.itens) == 0 
    
    def push(self, new):
        self.itens.append(new)
        
    def pop(self):
        return self.itens.pop()
    
    def __str__(self):
        return str(self.itens)
    
    def __len__(self):
        return len(self.itens)