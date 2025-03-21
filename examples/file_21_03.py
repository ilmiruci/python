# Как использовать функцию __import__


def exists_pyperclip() -> bool:
    try:
        import pyperclip
    except ModuleNotFoundError:
        return False

    return True


def exists_pyperclip_upd(module_name: str) -> bool:
    try:
        import module_name
        __import__(module_name)
    except ModuleNotFoundError:
        return False

    return True


if __name__ == '__main__':
    print(exists_pyperclip_upd('colorama'))
    print(exists_pyperclip_upd('pyperclip'))
    print(exists_pyperclip_upd('colorama2'))
