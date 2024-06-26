import math

while True:
    try:
        n = int(input())
        if n <= 0:
            break
        medida = input().split()
        h, c, l = map(int, medida)
        area = n * l * math.sqrt(h * 2 + c * 2) / 10000
        print("{:.4f}".format(area))  
    except ValueError:
        print("Entrada inválida. Certifique-se de inserir números inteiros.")
    except EOFError:
        break