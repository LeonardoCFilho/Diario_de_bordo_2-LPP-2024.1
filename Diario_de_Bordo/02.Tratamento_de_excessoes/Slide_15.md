### Tratadores de excessões
- Tratadores
  - 'try' e 'except'
    - [Exemplo](https://github.com/LeonardoCFilho/Diario_de_bordo_2-LPP-2024.1/blob/main/Codigos_e_Exemplos/02.Tratamento_de_excessoes/Slide_15/1.try_Except.py) e sua [saída no terminal](https://github.com/LeonardoCFilho/Diario_de_bordo_2-LPP-2024.1/blob/main/Codigos_e_Exemplos/02.Tratamento_de_excessoes/Slide_15/1.try_Except.png)
- Continuação após o erro
  - Indicativos
    - Python produz mensagens de erro para o programador durante a iteração do código ou durante sua escrita caso ocorram erros de sintaxe
  - Tratamento
    - O tratamento de excessões é feito pelo uso de 'try' e 'except', os quais permitem o programador tratá-la de forma personalizada
  - Especificação de excessão pelo programador
    - Excessões personalizadas podem ser criadas herdando da classe base 'Exception' ou de outra classe de excessão mais específica
    - Excessões personalizadas podem ser adaptadas para informar em qual parte do código a excessão aconteceu, mas em excessões pré-definidas isso não é possível
  - Pré definida
    - Há diversas excessões pré-definidas em Python e, enquanto a maioria, tem tratamento pré-definido, algumas requerem a intervenção do programador para serem solucionadas
    - Excessões pré-definidas podem ser lançadas pelo usuário através do uso de 'raise'
  - Temporariamente desligar excessões
    - É possível através do uso de um 'try' com apenas um 'except', o qual é mantido vazio
