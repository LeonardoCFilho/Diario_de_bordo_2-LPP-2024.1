def Quadrado(x):
    return x*x

def UsaFuncao(funcao,x):
    return funcao(x)
    
res = UsaFuncao(Quadrado,5)
print(res)