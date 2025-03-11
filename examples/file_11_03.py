# total_weight, M, k1, k2 = int(input()), int(input()), int(input()), int(input()),
# y = int((M - k2) * total_weight / (k1 - k2))
# weight_2 = int(total_weight - y)
# print(y, weight_2)


# Корень зла.
a, b, c = float(input()), float(input()), float(input())

if a == 0 and b == 0 and c == 0:
    print("Infinite solutions")
elif a == 0 and b != 0 and c != 0:
    x1 = -(c / b)
    print(f"{x1:.2f}")
elif a == b == 0:
    print("No solution")
elif a == c == 0:
    print(f"{0:.2f}")
else:
    D = (b ** 2) - (4 * a * c)

    if D == 0:
        x1 = -b / (2 * a)
        print(f"{x1:.2f}")
    elif D > 0:
        x1 = (-b + (D ** 0.5)) / (2 * a)
        x2 = (-b - (D ** 0.5)) / (2 * a)

        x1, x2 = min(x1, x2), max(x1, x2)
        print(f"{x1:.2f} {x2:.2f}")
    elif D < 0:
        print("No solution")
