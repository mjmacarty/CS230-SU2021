# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 17:36:07 2021

@author: MattMacarty
"""
A = input("Enter a value: ")
B = input("Enter another value: ")

print("The value of A is:", A)
print("The value of B is:", B)

print("=" * 20)

# placeholder = A
# A = B
# B = placeholder

A, B = B, A


print("The value of A is now :", A)
print("And B is:", B)