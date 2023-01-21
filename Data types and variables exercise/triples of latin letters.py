n = int(input())

symbol = 97

for first in range(symbol, symbol + n):
    for second in range(symbol, symbol + n):
        for third in range(symbol, symbol + n):
            print(chr(first), chr(second), chr(third), sep='')