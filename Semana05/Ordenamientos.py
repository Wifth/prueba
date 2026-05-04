def ordenInsercion(lst):
    n = len(lst)
    for pasada in range(1,n):
        posNueNum = pasada
        while posNueNum >= 1 and lst[posNueNum] < lst [posNueNum -1]:
            lst[posNueNum], lst[posNueNum - 1] = lst[posNueNum - 1], lst[posNueNum]
            posNueNum -=1
def ordenBurbuja(lst):
    n = len(lst)
    for pasada in range(n-1):
        for izqPar in range (n - 1 - pasada):
            derPar = izqPar + 1
            if lst[izqPar] > lst[derPar]:
                lst[izqPar], lst[derPar] = lst[derPar], lst[izqPar]

def ordenSeleccion(lst):
    n = len(lst)
    for manoIzq in range(n-1):
        posMenor = manoIzq
        for ver in range(manoIzq + 1, n):
            if lst[posMenor] > lst[ver]:
                posMenor = ver
        lst[manoIzq], lst[posMenor] = lst[posMenor], lst[manoIzq]



list = [2,8,5,3,9,4,1]
ordenBurbuja(list)
print(list)