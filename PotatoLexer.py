from potatoTokens import *


class PotatoLexer:
    def __init__(self, potato_code):
        self.p1: str = potato_code
        self.p2: int = 0
        self.p3 = -1

        self.next()

    def next(self):
        if self.p2 < len(self.p1):
            self.p3 = self.p1[self.p2]
            self.p2 += 1
        else:
            self.p3 = -1

    def potato(self):
        # - tokens - #
        output: tuple = tuple()
        while not (self.p3 == -1):
            if self.p3 in (' ', '\t', '\n'):
                if self.p3 == '\n':
                    output += (PotatoTokens(NEWLINE), )
                if self.p3 == '\t':
                    output += (PotatoTokens(TAB), )
                self.next()
            else:
                if self.p3 in CHAR1:
                    # - is character - #
                    output += (self.potato1(), )
                elif self.p3 in NUM:
                    # - is number - #
                    output += (self.potato2(), )
                elif self.p3 in Q:
                    # - is quotation mark - #
                    output += (self.potato3(), )
                else:
                    # - else - #
                    output += (self.potato4(), )
                self.next()

        self.p1, self.p2 = output, 0
        output: dict = {0: tuple()}
        ran: int = 0

        while len(self.p1) > self.p2:
            self.next()
            output[ran] += (self.p3, )
            if self.p3.get_type() == NEWLINE:
                ran += 1
                output.update({ran: tuple()})

        for i in output.keys():
            print(output[i]) if output[i] != tuple() else ...
        return output

    def potato1(self):
        # - char - #
        char = {'+': PLUS, '-': MIN, '*': MUL, '/': DIV, '%': MOD,
                '<': LESS, '>': GREATER, '&': AND, '|': OR, '!': NOT,
                '(': LB, ')': RB, '{': DO, '}': END, '[': LB2, ']': RB2,
                '.': DOT, '=': BE, ':': COLON, ';': COLON2, ',': COMMA,
                '\\': SLASH, '^': XOR, }
        out = char.get(self.p3)
        if out is not None:
            if out in (BE, MUL, DIV, LESS, GREATER):
                if char.get(self.p1[self.p2]) in (BE, MUL, DIV, LESS, GREATER):
                    char = {'<': SL, '>': SR, '=': EQUAL,
                            '*': POW, '/': DIV2}
                    out = (char.get(self.p1[self.p2]))
                    self.next()
            return PotatoTokens(out)
        else:
            quit(f'SyntaxError: invalid character >> ( {self.p3} )')

    def potato2(self):
        # - number - #
        out, ree = '', 0
        while not (self.p3 == -1):
            if (self.p3 in NUM) or (self.p3 == '.'):
                out += self.p3
                self.next()
            else:
                self.p2 -= 1
                break
        if '.' in out:
            return PotatoTokens(TT_FLT, str(float(out)))
        else:
            return PotatoTokens(TT_INT, str(int(out)))

    def potato3(self):
        # - string - #
        try:
            word: str = ''
            q = self.p3
            self.next()
            while True:
                if self.p3 == q:
                    self.p2 -= 1
                    break
                word += self.p3
                self.next()
            self.next()
            return PotatoTokens(TT_STR, word)
        except TypeError:
            quit('SyntaxError: unterminated string literal')

    def potato4(self):
        # - else - #
        out: str = ''
        while not (self.p3 == -1):
            if self.p3 in CHAR1:
                self.p2 -= 1
                break
            elif self.p3 in Q:
                self.p2 -= 1
                break
            elif self.p3 in (' ', '\n', '\t'):
                self.p2 -= 1
                break
            out += self.p3
            self.next()
        if out in KEY_WORLD:
            return PotatoTokens(TT_KEY, out)
        elif out in BOOLEAN:
            return PotatoTokens(TT_BOL, out)
        return PotatoTokens(TT_POT, out)
