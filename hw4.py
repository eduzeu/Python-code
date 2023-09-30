'''

Eduardo Hernandez
I pledge my honor that I have abided by the Stevens Honor System.

'''

def pascalSumList(pascalList):
    '''Returns the list of sums of adjacent terms in the original
    list'''
    
    if pascalList == []:
        return []
    elif len(pascalList) == 1:
        return [1]
    else:
        return [pascalList[0] + pascalList[1]]+ pascalSumList(pascalList[1:])

def pascal_row(n):
    '''Returns the list of numbers represented in rows  in pascal
    triangle starting from n = 0, to the nth term - 1.'''
    
    if n == 0:
        return [1]
    elif n == 1:
        return [1,1]
    else:
        return [1] + pascalSumList(pascal_row(n-1))


def pascal_triangle(n):
    '''that takes as input a single integer n and returns a
    list of lists containing the values of the all the rows up to
    and including row n'''
    
    if n == 0:
        return [[1]]
    elif n == 1:
        return [[1], [1,1]]
    else:
        return pascal_triangle(n-1) + [pascal_row(n)]

def test_pascal_row():
    '''tests the pascal_row function by using assertion '''
    
    assert pascal_triangle(0) == [[1]]
    assert pascal_triangle(1) == [[1],[1,1]]
    assert pascal_triangle(2) == [[1], [1, 1], [1, 2, 1]]
    assert pascal_triangle(3) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]

def test_pascal_triangle():
    '''tests the pascal_triangle function by using assertion  '''
    
    assert pascal_row(0) == [1]
    assert pascal_row(1) == [1,1]
    assert pascal_row(2) == [1, 2, 1]
    assert pascal_row(3) == [1, 3, 3, 1]
 
