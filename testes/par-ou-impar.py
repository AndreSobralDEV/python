import random

def gerar_numeros_aleatorios(n):
    numeros = [random.randint(1, 100) for _ in range(n)]
    return numeros

def verificar_par_ou_impar(numero):
    if numero % 2 == 0:
        return "par"
    else:
        return "ímpar"

def main():
    quantidade_numeros = int(input("Quantos números aleatórios você deseja gerar? "))
    numeros_aleatorios = gerar_numeros_aleatorios(quantidade_numeros)
    
    print("Números gerados:", numeros_aleatorios)
    
    for numero in numeros_aleatorios:
        paridade = verificar_par_ou_impar(numero)
        print(f"O número {numero} é {paridade}.")

if __name__ == "__main__":
    main()
