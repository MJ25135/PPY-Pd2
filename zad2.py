a = int(input("Podaj liczbę a: "))
b = int(input("Podaj liczbę b: "))

operator = input("Podaj znak operacji: ")

if operator == '+':
    result = int(a + b)
elif operator == '-':
    result = a - b
elif operator == '*':
    result = a * b
elif operator == '/':
    result = a / b
elif operator == '//':
    result = a // b
elif operator == '%':
    result = a - b
elif operator == '**':
    result = a - b

print(result)
