def decimal_to_binary(decimal: int) -> str:
    binary = ''
    while decimal // 2 > 0:
        binary = f'(decimal % 2)' + binary
        decimal //= 2
    return str(decimal) + binary

result = decimal_to_binary(1534)
print(result)
