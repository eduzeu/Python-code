def KFP(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return KFP(n-1) +  KFP(n-2) +  KFP(n-3)  

dic = {}
def KFP_FAST(n):
    if n in dic:
        return dic[n]
    if n == 1:
        dic[n] = 1
        return dic[n]
    elif n == 2:
        dic[n] = 2
        return dic[n]
    elif n == 3:
        dic[n] = 4
        return dic[n]
    else:
        stair1 = KFP_FAST(n-1) 
        dic[n-1] = stair1
        stair2 = KFP_FAST(n-2)
        dic[n-2] = stair2
        stair3 = KFP_FAST(n-3)
        dic[n-3] = stair3
        answer = stair1 + stair2 + stair3 
        return answer

mem = {( '' , 'st ' ): 0 , ( ' ' , 't ' ): 0 , ( 'a ' , ' ' ): 0 , ( 'a ' , 't ' ): 0 , ( 'a ' , ' st ' ): 0 , \
( ' ea ' , ' est ' ): 1 , ( ' tea ' , ' test ' ): 2}

mem [( 'a ' , 't ' )] = 8
print( ( 'e ' , 't ') in mem )
print( mem [( ' ea ' , ' est ' )] )
print( mem [( 'a ' , 't ' )] )


def dropWhile(odd, L, a=[]):
    if L==[]:
        return a
    else:
        if odd(L[0]):
            a = a+[L[0]]
            return dropWhile(odd, L[1:], a)
        else:
            return dropWhile(odd, L[1:], a)

def odd(x):
    return x%2==1


def fact(n, a = 1):
    if n == 0:
        return a
    elif n == 1:
        return a 
    else:
        return fact(n-1, a*n) 
