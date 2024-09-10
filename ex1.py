def is_fibonacci_number(n):
    if n < 0:
        return false
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    return b == n
num = int(input("Digite um numero: "))
if is_fibonacci_number(num):
    print(f"O número {num} pertence à sequência de Fibonacci.")
else:
    print(f"O número {num} não pertence à sequência de Fibonacci. ")