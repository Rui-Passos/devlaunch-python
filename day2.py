import random

# Lista de serviços (exemplo NOC)
servicos = ["payments", "auth", "db", "api"]
estados = ["UP", "DOWN"]

print("=== STATUS DOS SERVIÇOS ===")
total_down = 0


for servico in servicos:
    estado = random.choice(estados)

    if estado == "DOWN":
        print(f"ALERTA: {servico} está DOWN!")
    else:
        print(f"{servico} está UP")

print("\nVerificações concluídas")
