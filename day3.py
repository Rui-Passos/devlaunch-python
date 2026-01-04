import random

servicos = ["payment", "auth", "db", "api"]
estados = ["UP", "DOWN"]


def verificar_servico(nome):
    estado = random.choice(estados)
    return estado


print("=== Status dos Serviços ===")

total_down = 0

for servico in servicos:
    estado = verificar_servico(servico)

    if estado == "DOWN":
        print(f"ALERTA: {servico} está DOWN!")
        total_down += 1
    else:
        print(f"{servico} está UP!")

print(f"\nServiços DOWN: {total_down}")
