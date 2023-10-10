#December 2022
#Eduardo Hernandez
#I pledge my honor that I have abided by the Stevens Honor System.

import math

class QuadraticEquation(object):

    def __init__(self, a, b, c):
        '''constructor for quadratic equation in which a cannot equal 0'''

        if a == 0:
             raise ValueError ('Coefficient \'a\' cannot be 0 in a quadratic equation.') 
        else:
            self.__a = float(a)
            self.__b = float(b)
            self.__c = float(c)

    @property  
    def a(self):
        '''defining a'''
        return self.__a
    @property
    def b(self):
        '''defining b'''
        return self.__b
    @property
    def c(self):
        '''defining c'''
        return self.__c
    
    def discriminant(self):
        '''returns discriminant'''
    
        return self.__b ** 2 - 4 * self.__a * self.__c
    
    def root1(self):
        '''returns root square that will be aded after calculated'''
        discriminant = self.discriminant()
        if discriminant < 0:
            return None
        return (-1 * self.__b + math.sqrt(discriminant)) / (2 * self.__a)
                
    def root2(self):
        '''returns root square that will be subtracted after calculated'''
        discriminant = self.discriminant()
        if discriminant < 0:
            return None
        return (-1 * self.__b - math.sqrt(discriminant)) / (2 * self.__a)
                
    def __str__(self):
        '''returns quadratic equation'''
        if self.__a < 0:
            aSymbol = '-'
        else:
            aSymbol = ''
        if self.__b < 0 or self.__c < 0:
            bSymbol = '-'
        else:
            bSymbol = '+'
        if self.__c < 0:
            cSymbol = '-'
        else:
            cSymbol = '+'
        if self.__a == 1 or self.__a == -1:
            a = ''
        else:
            a = str(abs(self.__a))
        if self.__b == 0:
            b = ''
        elif self.__b == 1 or self.__b == -1:
            b = bSymbol + ' x '
        else:
            b = bSymbol + ' ' + str(abs(self.__b)) + 'x '
        if self.__c == 0:
            c = ''
        else:
            c = cSymbol + ' ' + str(abs(self.__c)) + ' '
            
        return aSymbol + a + 'x^2 ' + b + c + '= 0'    
            
