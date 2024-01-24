from PotatoLexer import PotatoLexer
from potatoParser import Parser


def interpreter(code):
    code = PotatoLexer(code).potato()
    code = Parser(code).potato()
    return code


if __name__ == '__main__':
    testCode = """
    potato1 potato2
    """
    interpreter(testCode)

    while True:
        c = input('>>> ')
        if c != 'end':
            print(interpreter(c))
            continue
        quit()
