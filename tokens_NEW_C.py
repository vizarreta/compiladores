import ply.lex as lex


# tokens_NEW_C.py

reserved = {
    'int': 'TYPE_INT',
    'float': 'TYPE_FLOAT',
    'String': 'TYPE_STRING',
    'boolean': 'TYPE_BOOL',
    'void': 'FUNCION',
    'return': 'RETURN',
    'for': 'BUCLE_FOR',
    'while': 'BUCLE_WHILE',
    'do': 'BUCLE_DO',
    'if': 'IF',
    'else': 'ELSE',
    'System': 'PRINT',
    'Scanner': 'READ',
    'true': 'TRUE',
    'false': 'FALSE',
    '&&': 'AND',
    '||': 'OR'
}

# Otros códigos de configuración del lexer...

tokens_list = list(reserved.values())  # Asegúrate de no tener errores de indentación aquí también

# Lista de nombres de tokens. Siempre es requerida.
tokens = [
    'ID',#
    'NUMERO',#
    'CADENA',#
    'SUMA',#
    'RESTA',#
    'DIVIDIR',#
    'MULTIPLICAR',#
    'COMENTARIO_LINEA',#
    'COMENTARIO_BLOQUE',#
    'PARENTESIS_ABIERTO',#
    'PARENTESIS_CERRADO',#
    'DECIMAL',#
    'LLAVE_ABIERTO',#
    'LLAVE_CERRADO',#
    'COMA',#
    'IGUAL',#
    'IGUAL_IGUAL',#
    'MENOR',#
    'MAYOR',#
    'MAYOR_IGUAL',
    'MENOR_IGUAL',
    'DIFERENTE',
    'PUNTO_COMA'
] + list(reserved.values())

# Reglas de expresión regular para los tokens simples
t_SUMA = r'\+'
t_RESTA = r'-'
t_DIVIDIR = r'/'
t_MULTIPLICAR = r'\*'
t_IGUAL = r'='
t_IGUAL_IGUAL = r'=='
t_PARENTESIS_ABIERTO = r'\('
t_PARENTESIS_CERRADO = r'\)'
t_LLAVE_ABIERTO = r'{'
t_LLAVE_CERRADO = r'}'
t_MENOR = r'<'
t_MENOR_IGUAL = r'<='
t_MAYOR = r'>'
t_MAYOR_IGUAL = r'>='
t_DIFERENTE = r'!='
t_COMA = r','
t_PUNTO_COMA = r';'


# Regla para identificar variables (identificadores)
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'ID')  # Verifica si es una palabra reservada

    return t


# Corrección en la expresión regular para t_DECIMAL
def t_DECIMAL(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

# Regla para detectar cadenas entre comillas dobles
def t_CADENA(t):
    r'"[^"]*"'  # Esto busca cualquier cosa entre comillas dobles.
    t.value = t.value[1:-1]  # Eliminamos las comillas dobles del valor.
    return t


# Regla de expresión regular para números enteros
def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)
    return t


# Regla para detectar comentarios de línea
def t_COMENTARIO_LINEA(t):
    r'--.*'
    pass  # Los comentarios de línea no generan tokens, simplemente los ignoramos.

def t_COMENTARIO_BLOQUE(t):
    r'/-[\s\S]*?-/'
    pass  # Los comentarios de bloque no generan tokens, simplemente los ignoramos.


# Definir una regla para rastrear números de línea
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Una cadena que contiene caracteres ignorados (espacios y tabulaciones)
t_ignore = ' \t'

# Regla de manejo de errores
def t_error(t):
    print(f"ESTE CARACTER NO SE ENCUENTRA'{t.value[0]}'")
    t.lexer.skip(1)

# Construir el analizador léxico
lexer = lex.lex()

class allTokens:

    def __init__(self, type, lexeme, line, column):
        self.type = type
        self.lexeme = lexeme
        self.line = line
        self.column = column


# llegamos al momento de la verdad la prueba pipipi
with open('ejemplo.txt', 'r') as archivo:
    codigo = archivo.read()

print("IMPRIMIENDO EL EJEMPLO:\n")
print(codigo)
print("_____________________________________________\n")

# Darle al analizador léxico una entrada
lexer.input(codigo)

# Crear una lista para almacenar los tokens como tuplas
tokens_list = []

# Tokenizar
while True:
    tok = lexer.token()
    if not tok:
        break  # No hay más entrada

    # Agregar el token como una instancia de allTokens a la lista de tokens
    t = allTokens(tok.type, tok.value, tok.lineno, tok.lexpos)
    tokens_list.append(t)

# Imprimir los tokens
print("\nTokens:\n")
print("_____________________________________________\n")
for token in tokens_list:
    print(
        f" LexToken({token.type},'{token.lexeme}',{token.line},{token.column})"
    )

# Agregar el token de final de archivo
dolar = allTokens("$", '', 0, 0)
tokens_list.append(dolar)

# Imprimir palabras clave
print("\nLAS PALABRAS CLAVE:\n")
print("_____________________________________________\n")
for token in tokens_list:
    print(f"{token.type}")

print("\nTODO ACEPTADO\n")

print("_____________________________________________")