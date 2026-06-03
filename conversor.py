# Conversor de Unidades
# Suporta: temperatura, distancia, peso e moeda

def converter_temperatura(valor, de, para):
    if de == para:
        return valor
    if de == "celsius":
        if para == "fahrenheit":
            return (valor * 9/5) + 32
        if para == "kelvin":
            return valor + 273.15
    if de == "fahrenheit":
        if para == "celsius":
            return (valor - 32) * 5/9
        if para == "kelvin":
            return (valor - 32) * 5/9 + 273.15
    if de == "kelvin":
        if para == "celsius":
            return valor - 273.15
        if para == "fahrenheit":
            return (valor - 273.15) * 9/5 + 32

def converter_distancia(valor, de, para):
    em_metros = {
        "metro": 1,
        "kilometro": 1000,
        "centimetro": 0.01,
        "milimetro": 0.001,
        "milha": 1609.34,
        "pe": 0.3048,
        "polegada": 0.0254,
    }
    if de not in em_metros or para not in em_metros:
        return None
    return valor * em_metros[de] / em_metros[para]

def converter_peso(valor, de, para):
    em_kg = {
        "kg": 1,
        "grama": 0.001,
        "libra": 0.453592,
        "onca": 0.0283495,
        "tonelada": 1000,
    }
    if de not in em_kg or para not in em_kg:
        return None
    return valor * em_kg[de] / em_kg[para]

def mostrar_menu():
    print("\n============================")
    print("   CONVERSOR DE UNIDADES")
    print("============================")
    print("1. Temperatura")
    print("2. Distancia")
    print("3. Peso")
    print("0. Sair")
    print("============================")

def menu_temperatura():
    opcoes = ["celsius", "fahrenheit", "kelvin"]
    print("\nUnidades disponiveis:", ", ".join(opcoes))
    de = input("De: ").strip().lower()
    para = input("Para: ").strip().lower()
    if de not in opcoes or para not in opcoes:
        print("Unidade invalida!")
        return
    try:
        valor = float(input("Valor: "))
    except ValueError:
        print("Valor invalido!")
        return
    resultado = converter_temperatura(valor, de, para)
    print(f"\nResultado: {valor} {de} = {resultado:.2f} {para}")

def menu_distancia():
    opcoes = ["metro", "kilometro", "centimetro", "milimetro", "milha", "pe", "polegada"]
    print("\nUnidades disponiveis:", ", ".join(opcoes))
    de = input("De: ").strip().lower()
    para = input("Para: ").strip().lower()
    try:
        valor = float(input("Valor: "))
    except ValueError:
        print("Valor invalido!")
        return
    resultado = converter_distancia(valor, de, para)
    if resultado is None:
        print("Unidade invalida!")
        return
    print(f"\nResultado: {valor} {de} = {resultado:.4f} {para}")

def menu_peso():
    opcoes = ["kg", "grama", "libra", "onca", "tonelada"]
    print("\nUnidades disponiveis:", ", ".join(opcoes))
    de = input("De: ").strip().lower()
    para = input("Para: ").strip().lower()
    try:
        valor = float(input("Valor: "))
    except ValueError:
        print("Valor invalido!")
        return
    resultado = converter_peso(valor, de, para)
    if resultado is None:
        print("Unidade invalida!")
        return
    print(f"\nResultado: {valor} {de} = {resultado:.4f} {para}")

def main():
    print("Bem-vindo ao Conversor de Unidades!")
    while True:
        mostrar_menu()
        escolha = input("Escolha uma opcao: ").strip()
        if escolha == "1":
            menu_temperatura()
        elif escolha == "2":
            menu_distancia()
        elif escolha == "3":
            menu_peso()
        elif escolha == "0":
            print("\nAte mais!")
            break
        else:
            print("Opcao invalida, tente novamente.")

if __name__ == "__main__":
    main()
