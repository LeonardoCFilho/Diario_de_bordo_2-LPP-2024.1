### Passagem de parâmetros
- Passagem por valor
  - [Exemplo](https://github.com/LeonardoCFilho/Diario_de_bordo_2-LPP-2024.1/blob/main/Codigos_e_Exemplos/01.Subprogramas/Slide_13/1.Passagem_Valor.py) e sua [saída no terminal](https://github.com/LeonardoCFilho/Diario_de_bordo_2-LPP-2024.1/blob/main/Codigos_e_Exemplos/01.Subprogramas/Slide_13/1.Passagem_Valor.png)
- Passagem por resultado
  - [Exemplo](https://github.com/LeonardoCFilho/Diario_de_bordo_2-LPP-2024.1/blob/main/Codigos_e_Exemplos/01.Subprogramas/Slide_13/2.Passagem_Resultado.py) e sua [saída no terminal](https://github.com/LeonardoCFilho/Diario_de_bordo_2-LPP-2024.1/blob/main/Codigos_e_Exemplos/01.Subprogramas/Slide_13/2.Passagem_Resultado.png)
- Passagem por valor-resultado
  - [Exemplo](https://github.com/LeonardoCFilho/Diario_de_bordo_2-LPP-2024.1/blob/main/Codigos_e_Exemplos/01.Subprogramas/Slide_13/3.Passagem_Valor-Resultado.py) e sua [saída no terminal](https://github.com/LeonardoCFilho/Diario_de_bordo_2-LPP-2024.1/blob/main/Codigos_e_Exemplos/01.Subprogramas/Slide_13/3.Passagem_Valor-Resultado.png)
  - Vantagens:
    - Permite a modificação de valores sem necessidade de um retorno explícito, com menor consumo de memória
  - Desvantagens:
    - Dificulta a commpreensão do código, também podendo causar mudanças indesejadas
- Passagem por referência
  - Não é possível em Python, pois a linguagem não permite a manipulação direta da memória
- Passagem por nome
  - Não é possível em Python, pois a linguagem faz a cópia dos valores enviados para a função, alterando os nomes usados no processo
- Macros e genêricos
  - Não há o conceito de macros e tipos genéricos em Python

### Verificação de tipo
- Em Python, o tipo de variável é dinâmica, então a verificação de tipo teria que ser manualmente feito pelo programador
- Na maioria dos casos, o uso de função para o tipo errado, causará a mudança do tipo da variável

### Arrays multidimensionais
- Mapeado em linhas
- Não altera a chamada em funções, já que a matriz como um todo é copiada

### Subprograma como parâmetros
- [Exemplo](https://github.com/LeonardoCFilho/Diario_de_bordo_2-LPP-2024.1/blob/main/Codigos_e_Exemplos/01.Subprogramas/Slide_13/4.Subprograma_Parametro.py) e sua [saída no terminal](https://github.com/LeonardoCFilho/Diario_de_bordo_2-LPP-2024.1/blob/main/Codigos_e_Exemplos/01.Subprogramas/Slide_13/4.Subprograma_Parametro.png)
- Tipo de amarração em Python é do tipo profunda
