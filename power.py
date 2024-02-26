#  Power of Two
# Write a program that takes an integer as input and returns true if the input is a power of two.
import math

Num = int(input("Enter an Integer:"))

#use the inary representation check.

if Num != 0:
   print (1 == bin(Num).count("1"))