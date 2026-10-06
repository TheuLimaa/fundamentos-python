"""
FUNDAMENTOS DE PYTHON — 5) Módulos e imports

Conceito: um "módulo" é só um arquivo .py que contém código reutilizável
(funções, variáveis). Outro arquivo pode IMPORTAR esse código, em vez de
copiar e colar.

É exatamente isso que você já viu (e usou) em tudo neste estudo:
    from src.config import API_KEY        (projeto cotacoes-financeiras)
    from envio.outlook import enviar_email (projeto tratamento-dados-sql)

A regra básica:
    from nome_do_arquivo import nome_da_funcao

(sem a extensão ".py" no nome do arquivo!)

Isso só funciona quando os dois arquivos estão na MESMA pasta (ou você usa um
caminho mais elaborado — igual o sys.path.insert que já usamos nos notebooks,
pra "ensinar" o Python a olhar outra pasta).

Não existe solução pronta aqui de propósito. Primeiro, complete as duas
funções em ferramentas.py (esse arquivo que está aqui do lado). Depois, volte
pra cá e importe elas.
"""

# ============================================================================
# Exercício — importar e usar
# ============================================================================
# 1) Importe a função "dobrar" do arquivo ferramentas.py
# 2) Importe a função "saudacao" do arquivo ferramentas.py
# 3) Chame as duas funções com valores à sua escolha e imprima os resultados

# escreva seus imports aqui, no topo do arquivo (por convenção, imports
# sempre ficam no começo do arquivo, antes de qualquer outro código)
from ferramentas import dobrar, saudacao

resultado1 = dobrar(10)
print(resultado1)

resultado2 = saudacao("Matheus")
print(resultado2)