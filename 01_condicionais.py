"""
FUNDAMENTOS DE PYTHON — 1) Condicionais (if / elif / else)

Conceito: um condicional deixa o código tomar uma decisão — "se isso for verdade,
faça X; senão, faça Y". É a base de qualquer lógica de negócio (igual o CASE WHEN
que você já usa em SQL — é a mesma ideia, só que em Python).

Sintaxe:
    if condicao:
        # roda isso se a condicao for True
    elif outra_condicao:
        # roda isso se a primeira for False mas essa for True
    else:
        # roda isso se nenhuma condicao anterior foi True

Repare: não tem chave {} nem ponto-e-vírgula — Python usa INDENTAÇÃO (espaços no
início da linha) pra saber o que está "dentro" do if. Isso é bem diferente de
outras linguagens, e é a causa mais comum de erro no começo.

Não existe solução pronta aqui de propósito. Tente, rode, erre, ajuste.
"""

# ============================================================================
# Exercício 1 — positivo, negativo ou zero
# ============================================================================
# Crie uma variável "numero" com qualquer valor (ex.: numero = -5).
# Escreva um if/elif/else que imprime "positivo", "negativo" ou "zero",
# dependendo do valor.

numero = -5
# escreva seu if/elif/else aqui


# ============================================================================
# Exercício 2 — maior ou menor de idade
# ============================================================================
# Crie uma variável "idade". Imprima "menor de idade" se for menor que 18,
# senão imprima "maior de idade".


# ============================================================================
# Exercício 3 — o maior de três números
# ============================================================================
# Crie três variáveis numéricas (a, b, c). Usando if/elif/else (sem usar a
# função pronta max()), descubra e imprima qual delas é a maior.


# ============================================================================
# Exercício 4 — classificar um veículo (conectando com o projeto de SQL)
# ============================================================================
# Crie uma variável "tipo_veiculo" com um destes valores: "carro", "moto",
# "caminhao" ou "onibus".
# Usando if/elif/else, imprima "leve" para carro/moto, e "pesado" para
# caminhao/onibus. Se vier qualquer outro valor, imprima "desconhecido".
#
# Dica: isso é o mesmo raciocínio do CASE WHEN que você já escreveu em SQL
# (sql/tratamento_abastecimento.sql) — só que agora em Python.
