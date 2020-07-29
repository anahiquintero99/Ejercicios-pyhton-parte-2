def conversion (pesos_type, dollar_value):
    pesos = float(input(f'¿Cuantos pesos {pesos_type} tienes? '))
    dollars = round(pesos / dollar_value, 2)
    print(f'Tienes ${dollars} dolares.')

menu = """
    BIENVENIDO AL CONVERSOR DE MONEDAS 💰
    
    1.- Peso Colombiano
    2.- Pesos Argentinos
    3.-Pesos Mexicanos

    Elige una opción:
    """

option = int(input(menu))

if option == 1:
    conversion('colombianos', 3875)
elif option == 2:
    conversion('argentinos', 65)
elif option == 3:
    conversion('mexicanos', 24)
else:
    print('Elige la opcion correcta')