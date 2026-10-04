"""
FUNDAMENTOS DE PYTHON — 6) Tratamento de erros (try / except)

Conceito: quando algo dá errado durante a execução (ex.: converter texto que
não é número, acessar uma chave que não existe, uma API fora do ar), o Python
"quebra" o programa com um erro (Exception). O try/except deixa você capturar
esse erro e decidir o que fazer, em vez do programa simplesmente parar.

Sintaxe:
    try:
        # código que PODE dar erro
    except TipoDoErro:
        # o que fazer SE der esse erro especifico

Você já viu isso em ação no rodar_semanal.py (se uma etapa falha, ele registra
no log em vez de travar tudo sem explicação) e no servidor_api.py (captura
erro de SQL inválido e devolve uma mensagem, em vez de derrubar o servidor).

Não existe solução pronta aqui de propósito. Tente, rode, erre, ajuste.
"""

# ============================================================================
# Exercício 1 — converter texto pra número, com segurança
# ============================================================================
texto = "abc"
# Tente converter "texto" pra número com int(texto) dentro de um try.
# Se der erro (ValueError), imprima "não é possível converter isso em número"
# em vez de deixar o programa quebrar.


# ============================================================================
# Exercício 2 — acessar uma chave que pode não existir
# ============================================================================
abastecimento = {"placa": "ABC1D23", "valor": 1150.0}
# Tente imprimir abastecimento["km_rodado"] (chave que não existe nesse
# dicionário) dentro de um try/except, capturando KeyError, e imprimindo
# "essa informação não está disponível" em vez de quebrar.


# ============================================================================
# Exercício 3 — ligando com o seu projeto real
# ============================================================================
# Pensa no scripts/extracao: se o simulador (API) não estiver rodando, o
# requests.post(...) gera um erro de conexão (requests.exceptions.ConnectionError).
# Escreva (só a ideia, não precisa rodar de verdade aqui) como você usaria um
# try/except em volta dessa chamada, pra imprimir uma mensagem amigável tipo
# "não consegui conectar na API, verifique se o servidor está rodando" em vez
# de deixar aparecer aquele traceback gigante que você já viu antes.
