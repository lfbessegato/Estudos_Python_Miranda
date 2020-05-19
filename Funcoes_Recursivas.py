def fatorial(n: int) -> int:
    # Caso Base
    if n == 1:
        return 1

    # Caso Recursivo
    return n * fatorial(n - 1)

if __name__ == "__main__":
    fat5 = fatorial(5)
    print(fat5)