# src/main.py
def calculate(expression: str) -> float:
    # Evaluamos la expresión, asegurándonos de que sea una suma
    parts = expression.split(" + ")
    # Convertimos los elementos a flotantes y los sumamos
    return sum(float(part) for part in parts)

