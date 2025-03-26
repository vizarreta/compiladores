import ply.lex as lex
import sys

# Lista de tokens
tokens = (
    'IDENTIFICADOR', 'NUM_ENTERO', 'NUM_DECIMAL',
    'OP_ARITMETICO', 'OP_RELACIONAL', 'OP_LOGICO',
    'PARENTESIS', 'LLAVE', 'PUNTO_COMA', 'PALABRA_CLAVE'
)

# Palabras clave
def t_PALABRA_CLAVE(t):
    r'\b(?:int|float|if|else|while|for|return|print|let|var|const)\b'
    t.type = 'PALABRA_CLAVE'
    return t

t_IDENTIFICADOR = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_NUM_ENTERO = r'\d+'
t_NUM_DECIMAL = r'\d+\.\d+'
t_OP_ARITMETICO = r'[+\-*/%]'
t_OP_RELACIONAL = r'==|!=|<=|>=|<|>'
t_OP_LOGICO = r'&&|\|\|'
t_PARENTESIS = r'[()]'
t_LLAVE = r'[{}]'
t_PUNTO_COMA = r';'

t_ignore_COMENTARIO = r'//.*'
t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Carácter ilegal '{t.value[0]}' en la línea {t.lineno}")
    t.lexer.skip(1)

# Construcción del lexer
lexer = lex.lex()

# Prueba del lexer
data = """
int x = 10;
float y = 3.14;
if (x > y) {
    print(x);
}
"""
lexer.input(data)
for tok in lexer:
    print(tok)
