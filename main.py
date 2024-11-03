def calcular_volume_pilar(largura, profundidade, altura):
    """Calcula o volume de um pilar dado suas dimensões."""
    return largura * profundidade * altura

def calcular_quantidade_pilares(volume_total, volume_pilar):
    """Calcula a quantidade de pilares necessária com base no volume total e no volume de um pilar."""
    return volume_total / volume_pilar

def main():
    print("Calculadora de Quantidade de Pilares")

    # Solicita as dimensões do pilar
    largura = float(input("Digite a largura do pilar (em metros): "))
    profundidade = float(input("Digite a profundidade do pilar (em metros): "))
    altura = float(input("Digite a altura do pilar (em metros): "))

    # Calcula o volume do pilar
    volume_pilar = calcular_volume_pilar(largura, profundidade, altura)
    print(f"O volume de um pilar é: {volume_pilar:.2f} m³")

    # Solicita o volume total a ser suportado
    volume_total = float(input("Digite o volume total a ser suportado (em metros cúbicos): "))

    # Calcula a quantidade de pilares
    quantidade_pilares = calcular_quantidade_pilares(volume_total, volume_pilar)
    print(f"A quantidade de pilares necessária é: {quantidade_pilares:.0f}")

if __name__ == "__main__":
    main()
