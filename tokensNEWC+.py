import ply.lex as lex

# Palabras reservadas en NewC+
reserved = {
    'entero'  : 'TYPE_INT',
    'decimal' : 'TYPE_FLOAT',
    'cadena'  : 'TYPE_STRING',
    'booleano' : 'TYPE_BOOL',
    'funcion'  : 'FUNCION',
    'retorna' : 'RETURN',
    'para'  : 'BUCLE_FOR',
    'mientras' : 'BUCLE_WHILE',
    'hacer' : 'BUCLE_DO',
    'si'  : 'IF',
    'sino' : 'ELSE',
    'sinosi' : 'ELSEIF',
    'imprimir' : 'PRINT',
    'leer' : 'READ',
    'y' : 'AND',
    'o' : 'OR',
    'hasta' : 'UNTIL',
    'paso' : 'INSTEP'
}

# Lista de tokens
tokens = [
    'ID',
    'NUMERO',
    'CADENA',
    'SUMA',
    'RESTA',
    'DIVIDIR',
    'MULTIPLICAR',
    'COMENTARIO_LINEA',
    'COMENTARIO_BLOQUE',
    'PARENTESIS_ABIERTO',
    'PARENTESIS_CERRADO',
    'DECIMAL',
    'LLAVE_ABIERTO',
    'LLAVE_CERRADO',
    'COMA',
    'IGUAL',
    'IGUAL_IGUAL',
    'MENOR',
    'MAYOR',
    'MAYOR_IGUAL',
    'MENOR_IGUAL',
    'DIFERENTE',
    'PUNTO_COMA'
] + list(reserved.values())

# Expresiones regulares para tokens

t_SUMA = r'\+'
t_RESTA = r'-'
t_DIVIDIR = r'/'
t_MULTIPLICAR = r'\*'
t_IGUAL = r'='
t_IGUAL_IGUAL = r'=='
t_PARENTESIS_ABIERTO = r'\('
t_PARENTESIS_CERRADO = r'\)'
t_LLAVE_ABIERTO = r'\{'
t_LLAVE_CERRADO = r'\}'
t_MENOR = r'<'
t_MENOR_IGUAL = r'<='
t_MAYOR = r'>'
t_MAYOR_IGUAL = r'>='
t_DIFERENTE = r'!='
t_COMA = r','
t_PUNTO_COMA = r';'

# Identificadores
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'ID')  # Verifica si es palabra clave
    return t

# Números decimales
def t_DECIMAL(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

# Cadenas
def t_CADENA(t):
    r'"[^"\n]*"'
    t.value = t.value[1:-1]
    return t

# Números enteros
def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Comentarios de línea
def t_COMENTARIO_LINEA(t):
    r'//.*'
    pass

# Comentarios de bloque
def t_COMENTARIO_BLOQUE(t):
    r'/\*[\s\S]*?\*/'
    pass

# Manejo de nuevas líneas
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Caracteres ignorados
t_ignore = ' \t'

# Manejo de errores
def t_error(t):
    print(f"Error léxico: Caracter no válido '{t.value[0]}'")
    t.lexer.skip(1)

# Definir __file__ para evitar errores en entornos restringidos
import sys
sys.modules['__main__'].__file__ = "new_c_plus_lexer.py"

# Construcción del analizador léxico
lexer = lex.lex()

# Prueba con código fuente de NewC+
codigo = '''
    entero x = 10;
    imprimir(x);
'''

lexer.input(codigo)

# Imprimir tokens reconocidos
print("Tokens reconocidos:")
while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)
