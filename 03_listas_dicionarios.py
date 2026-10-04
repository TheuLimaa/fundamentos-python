"""
FUNDAMENTOS DE PYTHON — 3) Listas e dicionários

Conceito: são as duas estruturas de dados mais usadas em Python.

LISTA: uma sequência ordenada de valores, acessada por POSIÇÃO (começando em 0).
    placas = ["ABC1D23", "XYZ9E88"]
    placas[0]              -> "ABC1D23" (primeiro item)
    placas.append("NEW1")  -> adiciona um item no final

DICIONÁRIO: um conjunto de pares "chave: valor", acessado pelo NOME da chave,
não pela posição.
    abastecimento = {"placa": "ABC1D23", "litros": 200.5, "valor": 1150.0}
    abastecimento["placa"]   -> "ABC1D23"
    abastecimento["litros"]  -> 200.5

Isso é exatamente o que vem de dentro de uma resposta de API em JSON — por
isso entender isso aqui, sem pandas no meio, ajuda a entender o que o pandas
está fazendo por trás dos panos quando você usa `pd.DataFrame(...)`.

Não existe solução pronta aqui de propósito. Tente, rode, erre, ajuste.
"""

# ============================================================================
# Exercício 1 — mexendo numa lista
# ============================================================================
placas = ["ABC1D23", "XYZ9E88", "QWE4R56"]
# a) Imprima o primeiro item da lista (posição 0)
# b) Adicione "LMN7P12" no final da lista, com .append(...)
# c) Imprima a lista inteira de novo, pra confirmar que o item novo entrou


# ============================================================================
# Exercício 2 — mexendo num dicionário
# ============================================================================
abastecimento = {"placa": "ABC1D23", "litros": 200.5, "valor": 1150.0}
# a) Imprima só o valor da chave "placa"
# b) Imprima só o valor da chave "valor"
# c) Adicione uma nova chave "km_rodado" com o valor 350 (igual você faria
#    numa lista, mas usando o nome da chave entre colchetes:
#    dicionario["nome_da_chave"] = valor)


# ============================================================================
# Exercício 3 — uma lista de dicionários (igual vem de uma API)
# ============================================================================
abastecimentos = [
    {"placa": "ABC1D23", "valor": 1150.0},
    {"placa": "XYZ9E88", "valor": 890.5},
    {"placa": "QWE4R56", "valor": 1320.0},
]
# Usando um for (do arquivo anterior) pra percorrer essa lista, some o "valor"
# de cada dicionário e imprima o total no final — sem usar pandas, só Python puro.
# Dica: lembra do "total = 0" antes do loop? Dentro do loop, cada "item" vai
# ser um dicionário — então item["valor"] pega o valor daquela linha.
