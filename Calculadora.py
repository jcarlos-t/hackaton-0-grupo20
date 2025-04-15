def main():
    print("Calculadora de Sumas (escribe 'c' para borrar, 'q' para salir)")
    while True:
        entrada = input("Escribe una operación (ej: 2 + 2): ").strip()

        if entrada.lower() == 'q':
            print("Saliendo de la calculadora.")
            break
        elif entrada.lower() == 'c':
            print("Operación borrada.")
            continue

        try:
            # Verificamos si la operación es una suma válida
            if '+' in entrada:
                operandos = entrada.split('+')
                operandos = [float(op.strip()) for op in operandos]
                resultado = sum(operandos)
                print(f"Resultado: {resultado}")
            else:
                print("Solo se permiten operaciones de suma. Intenta de nuevo.")
        except Exception as e:
            print(f"Error en la operación: {e}. Intenta de nuevo.")

if __name__ == "__main__":
    main()
