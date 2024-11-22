import os
import keyboard


def designPrincipal():
    print(f"""
        =============================================
                Simulador de Gasto Diario
        =============================================
        Seleccione una opción:

        1. Registrar nuevo gasto
        2. Listar gastos
        3. Calcular total de gastos
        4. Generar reporte de gastos
        5. Salir
        =============================================
        """)
    return int(input("Choose an option (1-5): "))


def designrecords():
    option = print(f"""
        =============================================
                    Registrar Nuevo Gasto
        =============================================
        Ingrese la información del gasto:

        - Monto del gasto:
        - Categoría (ej. comida, transporte, entretenimiento, otros):
        - Descripción (opcional):

        Ingrese 'S' para guardar o 'C' para cancelar.
        =============================================
        """)
        if (option == 's'): 
        