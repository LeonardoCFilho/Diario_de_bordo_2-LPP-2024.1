def SomaInt(x, y):
    try:
        resultado = int(x) + int(y)
        return resultado
    except ValueError: #Conversão de alguma das variáveis para int não foi possível
        raise TypeError("Erro, tipos invalidos!")


print("Resultado da soma:", SomaInt(2, 4)) #int e int
print("Resultado da soma:", SomaInt(2, 3.1415)) #int e float -> erro conversão imprópria cria um resultado errado
print("Resultado da soma:", SomaInt("12", "13")) #string e String -> ambas representam um int, por isso não dá erro
print("Resultado da soma:", SomaInt("Hello", "World")) #string e String -> erro
