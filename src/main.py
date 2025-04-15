import re

# Funciones para las operaciones
def sumar(a, b):
    rreturn ...

def restar(a, b):
    return ...

def multiplicar(a, b):
    return ...

def dividir(a, b):
    return ...

# Función principal de cálculo
def calculate(expression):
    # Limpiar espacios extras
    expression = expression.replace(" ", "")

    # Validar que la expresión no esté vacía o solo contenga espacios
    if not expression:
        raise ValueError("Entrada vacía o solo con espacios")

    # Validar que no haya caracteres no válidos
    if not re.match(r'^[\d\+\-\*\/\.\(\)]+$', expression):
        raise ValueError("Caracteres no válidos en la expresión")

    # Separar la expresión en componentes: números y operadores
    tokens = re.split(r'(\+|\-|\*|\/|\(|\))', expression)
    tokens = [token for token in tokens if token.strip() != '']  # Eliminar espacios vacíos

    # Convertir los números de tokens a flotantes
    for i in range(len(tokens)):
        if tokens[i].replace('.', '', 1).isdigit():  # Verifica si es un número
            tokens[i] = float(tokens[i])

    # Función para evaluar la expresión paso a paso (sin usar eval)
    def eval_tokens(tokens):
        # Primero resolver multiplicaciones y divisiones (de izquierda a derecha)
        idx = 0
        while idx < len(tokens):
            if tokens[idx] == '*' or tokens[idx] == '/':
                left = tokens[idx-1]
                right = tokens[idx+1]
                if tokens[idx] == '*':
                    result = multiplicar(left, right)
                elif tokens[idx] == '/':
                    result = dividir(left, right)
                # Reemplazamos los elementos con el resultado de la operación
                tokens[idx-1:idx+2] = [result]
                idx -= 1  # Volver a comprobar desde el resultado
            else:
                idx += 1

        # Luego resolver sumas y restas
        idx = 0
        while idx < len(tokens):
            if tokens[idx] == '+' or tokens[idx] == '-':
                left = tokens[idx-1]
                right = tokens[idx+1]
                if tokens[idx] == '+':
                    result = sumar(left, right)
                elif tokens[idx] == '-':
                    result = restar(left, right)
                # Reemplazamos los elementos con el resultado de la operación
                tokens[idx-1:idx+2] = [result]
                idx -= 1  # Volver a comprobar desde el resultado
            else:
                idx += 1

        return tokens[0]  # El resultado final estará al principio

    # Evaluamos los tokens
    result = eval_tokens(tokens)

    return result
