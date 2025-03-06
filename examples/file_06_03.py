char_mapping: dict[str, list[str]] = {
    "a": ["5", "6", "7"],
    "b": ["1", "9", "0"],
    "c": ["3", "2", "8"],
}

# for data in char_mapping.items():
#     a, b = [10, 20]
#     key, value = data

char = "9"
for key, value, in char_mapping.items():
    # print(f"Ключ={key}")
    # print(f"Значение={value}")
    # print("----------")
    if char in value:
        print(f"Ключ найден: {key}")
        break

# ---------------------------

# 0-9
# 15 // 6
# 15 % 6

# 15 // 10  # 1
# 15 % 10  # 5

6784 % 10  # 4
6784 // 1000  # 6
6784 // 100  # 67
6784 // 100 % 10  # 7
6784 // 10 % 10  # 8

# Попробуйте получить все цифры у 5-значного числа.
# Попробуйте получить все цифры у N-значного числа. Гарантируется, что число натуральное.

# ---------------------------

s = 'python'
print(s.ljust(16, '#'))
print(s.rjust(16, '.'))
print(s.center(16, '~'))
print(s.zfill(10))

h = 1
m = 6
s = 9

print(f"{h:0>2}:{m:0>2}:{s:0>2}")

# ---------------------------

print(int("0045"))
print(int("1101"))
print(int("1101", 2))
print(int("1101", 8))
print(int("1101", 10))
print(int("1101", 16))
