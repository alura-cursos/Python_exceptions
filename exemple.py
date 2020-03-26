def dividir(dividendo, divisor):
    # print(divisor.resultado)
    return dividendo/divisor

def testa_divisao(divisor):
        resultado = dividir(10,divisor)
        print(f"O resultado da divisão de 10 por {divisor} é {resultado}")

try:
    testa_divisao(0)
except ZeroDivisionError as E:
    print("Erro de atributo tratado")
except Exception as E:
    print("Tratamento genérico")

print("Programa encerrado")