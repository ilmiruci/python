from typing import Any

# --------------Списки

nums: list[int] = [10, 20, 30, 40]

print(nums[1])
print(20 in nums)
nums[1] = 50
print(nums[1])

# --------------Словари

# ключ1: значение1, ключ2: значение2 ..., ключN: значениеN
fruits = {
    "яблоко": 5,
    "клубника": 10,
    "киви": 188,
    True: "Описание",
    False: "Описание 2",
    1: "один",  # дублирование ключа, True == 1
    2: "два",
    5: "пять",
    (10, 20, 30): "тут числа в кортеже",
    # [10, 20, 30]: "Изменяемые типы не могут быть ключами в словаре",
    # "яблоко": 16,  # ключи должны быть уникальными
}

print(fruits)
print(fruits.keys())
print(fruits.values())
print(fruits.items())

print(5 in fruits)
print(len(fruits))

print(fruits["клубника"])
print(fruits[(10, 20, 30)])
print(fruits[True])
print(fruits[False])
print(fruits.get("клубника"))

# print(fruits.get("банан", "Такой ключ нет"))
# print(fruits["банан"])
#
# print(fruits)

fruits["банан"] = 20
fruits["киви"] = 150
print(fruits.get("банан", "Такой ключ нет"))
print(fruits["банан"])

print(fruits)

# Аннотация типов в словарях
ex_1: dict = {"alice": 18, "bob": 20}
ex_2: dict[str, int] = {"alice": 18, "bob": 20}


fruits: dict[Any, Any] = {
    "яблоко": 5,
    False: "Описание 2",
    5: "пять",
    (10, 20, 30): "тут числа в кортеже",
}
