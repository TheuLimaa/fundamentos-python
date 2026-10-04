"""
FUNDAMENTOS DE PYTHON — 4) Funções

Conceito: uma função empacota um pedaço de código, dá um NOME a ele, e permite
reusar esse código quantas vezes quiser, com entradas (parâmetros) diferentes
a cada vez — sem copiar e colar.

Sintaxe:
    def nome_da_funcao(parametro1, parametro2):
        resultado = parametro1 + parametro2
        return resultado

    # pra usar:
    soma = nome_da_funcao(2, 3)   # soma vira 5

Partes importantes:
- "def" começa a definição da função
- o que está entre parênteses são os PARÂMETROS — as "entradas" que a função
  recebe (podem ser 0, 1 ou vários)
- "return" é o que a função DEVOLVE como resultado. Se não tiver return, a
  função não devolve nada útil (devolve None)
- definir a função não roda nada ainda — só roda quando você CHAMA ela,
  escrevendo o nome + parênteses com os valores reais

Isso é literalmente o que você já viu em todo canto do seu projeto (ex.:
`def extrair(sql_query):` em extracao/buscar_dados.py) — aqui vamos construir
do zero pra entender por dentro.

Não existe solução pronta aqui de propósito. Tente, rode, erre, ajuste.
"""

# ============================================================================
# Exercício 1 — função simples com dois parâmetros
# ============================================================================
# Escreva uma função chamada "somar" que recebe dois números e devolve a soma
# deles. Depois, CHAME essa função com dois números quaisquer e imprima o
# resultado.


# ============================================================================
# Exercício 2 — função que recebe uma lista
# ============================================================================
# Escreva uma função chamada "media" que recebe uma lista de números e
# devolve a média deles (soma dividida pela quantidade de itens).
# Dica: use o que você já sabe de loop (ou a função pronta sum() e len()).
# Teste com: media([10, 20, 30]) -> deveria devolver 20.0


# ============================================================================
# Exercício 3 — função ligada ao seu projeto real
# ============================================================================
# Escreva uma função chamada "calcular_valor" que recebe "litros" e
# "preco_por_litro", e devolve o valor total (litros * preco_por_litro).
# Teste com alguns valores diferentes.


# ============================================================================
# Exercício 4 — enxergando a função como "empacotar código repetido"
# ============================================================================
# Olhe esse código (com repetição óbvia):
#
#     idade_joao = 15
#     if idade_joao < 18:
#         print("João é menor de idade")
#     else:
#         print("João é maior de idade")
#
#     idade_maria = 22
#     if idade_maria < 18:
#         print("Maria é menor de idade")
#     else:
#         print("Maria é maior de idade")
#
# Transforme isso numa função "checar_idade(nome, idade)" que faz esse
# print sozinha, e chame ela duas vezes (uma pra João, outra pra Maria) —
# sem repetir o if/else duas vezes no código.
