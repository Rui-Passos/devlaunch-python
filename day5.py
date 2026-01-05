# Escrita em ficheiro
with open("status.log", "w") as f:
    f.write("payments: UP\n")
    f.write("auth: DOWN\n")

# Leitura do ficheiro
print("=== CONTEÚDO DO FICHEIRO ===")
with open("status.log", "r") as f:
    for linha in f:
        print(linha.strip())
