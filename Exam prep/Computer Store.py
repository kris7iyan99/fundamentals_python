def calculate_tax(price):
    return price * 0.2

def print_receipt(total_price_without_tax, is_special):
    total_tax = sum(map(calculate_tax, total_price_without_tax))
    total_price_with_tax = sum(total_price_without_tax) + total_tax
    if is_special:
        total_price_with_tax *= 0.9
    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {sum(total_price_without_tax):.2f}$")
    print(f"Taxes: {total_tax:.2f}$")
    print(f"Total price: {total_price_with_tax:.2f}$")

total_price_without_tax = []
while True:
    try:
        price = float(input())
        if price <= 0:
            print("Invalid price!")
            continue
        total_price_without_tax.append(price)
    except:
        customer_type = input()
        if customer_type == "regular":
            print_receipt(total_price_without_tax, False)
        elif customer_type == "special":
            if len(total_price_without_tax) == 0:
                print("Invalid order!")
            else:
                print_receipt(total_price_without_tax, True)
        else:
            print("Invalid input!")