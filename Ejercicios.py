

# The next code works in Python >= 3.0


######## Exercise 1
def parentesisBalanceados(pos,n,nOpen,nClose):
    global cadena
    if(nClose == n):
        print(cadena)
        return
    else:
        if(nOpen > nClose):
            cadena[pos] ='}'
            parentesisBalanceados(pos+1,n,nOpen,nClose+1)
        if(nOpen<n):
            cadena[pos] ='{'
            parentesisBalanceados(pos+1,n,nOpen+1,nClose)

n = 3
cadena = [0 for _ in range(2*n)]
print("Parentesis balanceados")
parentesisBalanceados(0,n,0,0)


######## Exercise 2
# The next code works in Python >= 3.0
def imprimeNSubstring(s,pos):
    size = len(s)
    array = []
    for i in range (size):
        for long in range (i+1,size+1):
            array.append( s[i:long] )

    finalArray = []
    for e in sorted(array):
        finalArray.append(e)

    r = ''
    for i in finalArray:
        r += i

    print(r[pos-1])

print("Substrings")
imprimeNSubstring( "dbac",3)

######## Exercise 3
# The next code works in Python >= 3.0
import math

def super_digit(num):
    sumR = 0
    while (num > 0 or sumR > 9):
        if (num == 0):
            num= sumR
            sumR = 0
        sumR += num%10
        num = math.floor(num /10 )
    return sumR

digit = 148
times = 3
res = int( str(digit)*times )

print("Super digitos")
print(super_digit(res))



