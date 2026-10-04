"""
FUNDAMENTOS DE PYTHON — 2) Loops (for / while)

Conceito: um loop repete um bloco de código várias vezes, sem você precisar
copiar e colar a mesma linha. É assim que, por exemplo, o pandas/SQL processam
milhares de linhas sem você escrever milhares de instruções.

Dois tipos principais:

    for item in uma_lista:
        # roda uma vez pra cada item da lista

    while condicao:
        # roda repetidamente ENQUANTO a condição for True
        # (cuidado: se a condição nunca virar False, o loop nunca para!)

Não existe solução pronta aqui de propósito. Tente, rode, erre, ajuste.
"""

# ============================================================================
# Exercício 1 — contar de 1 a 10
# ============================================================================
# Use um for com range(...) para imprimir os números de 1 a 10, um por linha.
# Dica: range(1, 11) gera os números de 1 até 10 (o segundo número NÃO entra).


# ============================================================================
# Exercício 2 — soma de 1 a 100
# ============================================================================
# Sem usar nenhuma função pronta de soma, use um for pra somar todos os
# números de 1 a 100 e imprimir o resultado no final.
# Dica: crie uma variável "total = 0" antes do loop, e vá somando dentro dele.


# ============================================================================
# Exercício 3 — percorrer uma lista de placas
# ============================================================================
placas = ["ABC1D23", "XYZ9E88", "QWE4R56", "LMN7P12"]
# Use um for pra imprimir cada placa dessa lista, uma por linha.


# ============================================================================
# Exercício 4 — contar quantos abastecimentos passaram de um valor
# ============================================================================
valores = [120.50, 340.00, 89.90, 410.00, 75.30, 300.00]
# Usando um for + um if dentro dele, conte quantos valores dessa lista são
# maiores que 200. Imprima a contagem no final.
# Dica: crie uma variável "contador = 0" antes do loop, e some 1 toda vez que
# a condição do if for verdadeira.
