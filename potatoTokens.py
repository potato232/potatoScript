"""
# - Arithmetic Operators - #
PLUS, MIN, MUL, DIV, MOD = '+', '-', '*', '/', '%'
POW, DIV2 = '**', '//'

# - Comparison Operators - #
EQUAL, GREATER, LESS = '==', '<', '>'

# - Bitwise Operators - #
AND, OR, NOT = '&', '|', '!'
XOR, SL, SR  = '^', '<<', '>>'

# - #
SL, SR, EQUAL, POW, DIV2
# - #
"""

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
