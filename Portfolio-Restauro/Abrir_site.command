#!/bin/bash

# 1. Navega para a pasta onde o ficheiro está guardado
cd "$(dirname "$0")"

echo "------------------------------------------------"
echo "A iniciar o site da Inês... Não feches esta janela!"
echo "------------------------------------------------"

# 2. Ativa o ambiente virtual
# No Mac o caminho é venv/bin/activate
source venv/bin/activate

# 3. Instala as dependências (caso tenhas mudado de PC)
pip install -r requirements.txt

# 4. Abre o site automaticamente no teu browser padrão
open "http://127.0.0.1:5000"

# 5. Corre o servidor Python
python3 app.py