def TrocaValores(vetorInt):
    x = vetorInt[0]
    vetorInt[0] = vetorInt[1] 
    vetorInt[1] = x

vetorInt = [1,2]
print(vetorInt)
TrocaValores(vetorInt)
print(vetorInt)