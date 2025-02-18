def say_hello(name: str) -> str:
    return f"Привет, {name}!"


def example() -> None:
    print("Hi!")

    return
    # return None


# print(__name__)


if __name__ == '__main__':
    print(example())
    # print(say_hello(input("Введите тествоое имя: ")))
    # print(2 + 3)
