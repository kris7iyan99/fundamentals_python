def orders (product, quantity):
    result = 0
    if product == 'coffee':
        result = 1.5 * quantity
    elif product == 'water':
        result = 1 * quantity
    elif product == 'coke':
        result = 1.4 * quantity
    elif product == 'snacks':
        result = 2 * quantity

    return result


res = orders(product = input(), quantity = int(input()))
print(f'{res:.2f}')


