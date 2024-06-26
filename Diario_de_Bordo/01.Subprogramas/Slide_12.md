### Definções básicas 
- Cabeçalho de subprograma
  - Em Python, o cabeçalho para uma função é definida como: def <nome da função>(< valores recebidos >):
  - [Exemplo](https://github.com/LeonardoCFilho/Diario_de_bordo_2-LPP-2024.1/blob/main/Codigos_e_Exemplos/01.Subprogramas/Slide_12/1.Exemplo_Funcao.py) e sua [saída no terminal](https://github.com/LeonardoCFilho/Diario_de_bordo_2-LPP-2024.1/blob/main/Codigos_e_Exemplos/01.Subprogramas/Slide_12/1.Exemplo_Funcao.png)
- Acesso de dados
 - É possível editar uma varáivel global em Python através do uso prefixo 'global' 
 - Edição de valores recebidos
   - Listas e dicionários podem ser diretamente alterados na função, alterando seu valor
   - Variáveis como int e strings podem ser diretamente alterados na função, mas o valor será alterado apenas na função, não em sua posicação original  

### Definição vs declaração
- Python não permite referência futura
- [Exemplo](https://github.com/LeonardoCFilho/Diario_de_bordo_2-LPP-2024.1/blob/main/Codigos_e_Exemplos/01.Subprogramas/Slide_12/2.Referencia_Futura.py) e sua [saída no terminal](https://github.com/LeonardoCFilho/Diario_de_bordo_2-LPP-2024.1/blob/main/Codigos_e_Exemplos/01.Subprogramas/Slide_12/2.Referencia_Futura.png)

### Funções e procedimentos
- Procedimento
  - Altera diretamente
  - [Exemplo](https://github.com/LeonardoCFilho/Diario_de_bordo_2-LPP-2024.1/blob/main/Codigos_e_Exemplos/01.Subprogramas/Slide_12/3.Procedimento.py) e sua [saída no terminal](https://github.com/LeonardoCFilho/Diario_de_bordo_2-LPP-2024.1/blob/main/Codigos_e_Exemplos/01.Subprogramas/Slide_12/3.Procedimento.png)
- Função
  - Retorna o resultado
  - [Exemplo](https://github.com/LeonardoCFilho/Diario_de_bordo_2-LPP-2024.1/blob/main/Codigos_e_Exemplos/01.Subprogramas/Slide_12/4.Funcao.py) e sua [saída no terminal](https://github.com/LeonardoCFilho/Diario_de_bordo_2-LPP-2024.1/blob/main/Codigos_e_Exemplos/01.Subprogramas/Slide_12/4.Funcao.png)

### Parâmetros
- Mais flexível que subprogramas
- Parâmetros formais e reais
  - [Exemplo](https://github.com/LeonardoCFilho/Diario_de_bordo_2-LPP-2024.1/blob/main/Codigos_e_Exemplos/01.Subprogramas/Slide_12/4.Funcao.py) e sua [saída no terminal](https://github.com/LeonardoCFilho/Diario_de_bordo_2-LPP-2024.1/blob/main/Codigos_e_Exemplos/01.Subprogramas/Slide_12/4.Funcao.png)
    - Nesse exemplo, a primeira linha apresenta o parâmetro formal
    - Além disso, na sexta linha, o parâmetro real é usado
- Parâmetros nomeados
  - Python permite o de parâmetros posicionais ou como nomeado
  - [Exemplo](https://github.com/LeonardoCFilho/Diario_de_bordo_2-LPP-2024.1/blob/main/Codigos_e_Exemplos/01.Subprogramas/Slide_12/5.Parametro_nomeado.py) e sua [saída no terminal](https://github.com/LeonardoCFilho/Diario_de_bordo_2-LPP-2024.1/blob/main/Codigos_e_Exemplos/01.Subprogramas/Slide_12/5.Parametro_nomeado.png)
- Valores padrões
  - [Exemplo](https://github.com/LeonardoCFilho/Diario_de_bordo_2-LPP-2024.1/blob/main/Codigos_e_Exemplos/01.Subprogramas/Slide_12/6.Valores_padroes.py) e sua [saída no terminal](https://github.com/LeonardoCFilho/Diario_de_bordo_2-LPP-2024.1/blob/main/Codigos_e_Exemplos/01.Subprogramas/Slide_12/6.Valores_padroes.png)

### Parâmetro variádico 
- Permitido através do uso de prefixo no cabeçalho
  - '*' para tuple
  - '**' para dicionários 
- [Exemplo](https://github.com/LeonardoCFilho/Diario_de_bordo_2-LPP-2024.1/blob/main/Codigos_e_Exemplos/01.Subprogramas/Slide_12/7.Parametro_Variadico.py) e sua [saída no terminal](https://github.com/LeonardoCFilho/Diario_de_bordo_2-LPP-2024.1/blob/main/Codigos_e_Exemplos/01.Subprogramas/Slide_12/7.Parametro_Variadico.png)

### Variáveis locais & subprogramas aninhados
- Variáveis locais em Python são definidas como pilha-dinâmica
- Subprogramas aninhados
  - Feito em Python através da definição de uma função dentro de outra
  - A função criada (interna) pode ser chamada apenas pela função original
  - [Exemplo](https://github.com/LeonardoCFilho/Diario_de_bordo_2-LPP-2024.1/blob/main/Codigos_e_Exemplos/01.Subprogramas/Slide_12/8.Funcao_aninhada.py) e sua [saída no terminal](https://github.com/LeonardoCFilho/Diario_de_bordo_2-LPP-2024.1/blob/main/Codigos_e_Exemplos/01.Subprogramas/Slide_12/8.Funcao_aninhada.png)
