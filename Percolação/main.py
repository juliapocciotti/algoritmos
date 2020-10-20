#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 12:32:33 2020

@author: julia
"""
from percolation import Percolation

def main():
    sis1 = Percolation(1)
    
    sis2 = Percolation(2)
    
    sis3 = Percolation((3,2))
    
    sis4 = Percolation((3, 4))
    
    print(sis1.shape)
    print(sis2.shape)
    print(sis3.shape)
    print(sis4.shape)
    
    print(sis1)
    print(sis2)
    print(sis3)
    print(sis4)
    

main()