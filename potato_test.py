# - key word - #
IF, VAR, FUN, DEL, RE, IMPORT = 'if', 'var', 'fun', 'del', 'import', 'return'
KEY_WORLD = (IF, VAR, FUN, DEL, RE, IMPORT)

TRUE, FALSE, NULL = 'true', 'false', 'null'
BOOLEAN = (TRUE, FALSE, NULL)

# - #

PLUS, MIN, MUL, DIV, MOD = ('plus', 'min', 'mul', 'div', 'modulus')
POW, DIV2 = ('power', 'DivFloat')
Arithmetic = (PLUS, MIN, MUL, DIV, MOD, POW, DIV2)

# - #

EQUAL, GREATER, LESS = 'equal', 'greater', 'less'
XOR, SL, SR = 'XOR', 'ShiftLeft', 'ShiftRight'
AND, OR, NOT = 'AND', 'OR', 'NOT'

Comparison = (EQUAL, GREATER, LESS)
Bitwise = (XOR, SL, SR, AND, OR, NOT)

# - #

LB, RB, COMMA, DOT, COLON, COLON2 = ('LB', 'RB', 'COMMA', 'DOT', 'COLON', 'SemiColon')
BE, DO, END, RB2, LB2, SLASH = ('BE', 'DO', 'END', 'LB2', 'RB2', 'Slash')
NEWLINE, TAB = 'NEWLINE', 'TAB'

# - #

Q = ('\'', '\"')

NUM = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')

CHAR1 = ('+', '-', '*', '/', '%', '<', '>', '&', '|', '!',
         '^', '@', '#', '$', '.', '=', ':', ';', ',', '?',
         '(', ')', '{', '}', '[', ']', '`', 'π', '£', '¢',
         '~', '÷', '×', '‘', '√', '\\', '⟨', '⟩', '¡', '¿',
         '⁀', '/', '‘', '’', '“', '”', '±', '‰', '℮', '…',)

CHAR2 = (PLUS, MIN, MUL, DIV, MOD, EQUAL, GREATER, LESS,
         XOR, SL, SR, AND, OR, NOT, LB, RB, COMMA, DOT,
         COLON, COLON2, BE, DO, END, LB2, RB2, SLASH)

# - data type - #
TT_INT = 'INT'
TT_STR = 'STR'
TT_FLT = 'FLOAT'
TT_BOL = 'BOOL'
TT_ARR = 'LIST'
TT_KEY = 'KW'
TT_POT = 'NAME'


# - tokens - #
class PotatoTokens:
    def __init__(self, type_, value=None):
        self.t, self.v = type_, value

    def get_value(self):
        return self.v

    def get_type(self):
        return self.t

    def __repr__(self):
        if self.v is not None:
            return f'({self.t} : {self.v})'
        return f'({self.t})'




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
