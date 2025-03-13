total_sale: float = 0
sale: float = float(input("> "))
while sale:
    total_sale += sale - (sale * 0.1) if sale >= 500 else sale

    print(total_sale)

    sale = float(input("> "))

# -------------


n = 20
print(n)
# print(n=20)  # ошибка

# m := 30  # ошибка
print(m := 30)
