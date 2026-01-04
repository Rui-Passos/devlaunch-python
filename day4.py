import random

# Dados Base
SERVICOS = ["payments", "auth", "db", "api"]
ESTADOS = ["UP", "DOWN"]


def verificar_servicos(lista_servicos):
    resultados = []
    for servico in lista_servicos:
        estado = random.choice(ESTADOS)
        resultados.append({
            "servico": servico,
            "estado": estado
        })
    return resultados


def gerar_relatorio(resultados):
    total_down = 0
    total_up = 0

    print("=== RELATÓRIO DE SERVIÇOS ===")

    for item in resultados:
        if item["estado"] == "DOWN":
            print(f"ALERTA: {item['servico']} está DOWN!")
            total_down += 1
        else:
            print(f"{item['servico']} está UP")
            total_up += 1

    print(f"\nServiços DOWN: {total_down}")
    print(f"\nServiços UP: {total_up}")


def main():
    resultados = verificar_servicos(SERVICOS)
    gerar_relatorio(resultados)


# Pont de entrada do programa
main()
