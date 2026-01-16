#!/bin/bash

# Move o terminal para a pasta onde o ficheiro está
cd "$(dirname "$0")"

echo "A iniciar o servidor... Por favor aguarda."

# Ativa o ambiente virtual
if [ -d "venv" ]; then
    source venv/bin/activate
else
    echo "Erro: Pasta venv não encontrada. Cria o ambiente primeiro."
    exit 1
fi

# Instala o Flask se não estiver instalado (segurança extra)
pip install flask

# Abre o browser
open "http://127.0.0.1:5000"

# Corre o Python
python3 app.py