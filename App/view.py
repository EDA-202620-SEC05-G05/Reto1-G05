import sys
from tabulate import tabulate
from App import logic

default_limit = 1000
sys.setrecursionlimit(default_limit * 10)


def new_logic():
    """
        Se crea una instancia del controlador
    """
    control = logic.new_logic()
    return control

def print_menu():
    print("Bienvenido")
    print("0- Cargar información")
    print("1- Ejecutar Requerimiento 1")
    print("2- Ejecutar Requerimiento 2")
    print("3- Ejecutar Requerimiento 3")
    print("4- Ejecutar Requerimiento 4")
    print("5- Ejecutar Requerimiento 5")
    print("6- Ejecutar Requerimiento 6")
    print("7- Salir")

def load_data(control):
    """
    Carga los datos
    """
    filename = "Data/chocolate_sales/chocolate_sale_100_elementos.csv"
    result = logic.load_data(control, filename)

    print(f"\nTiempo de carga: {result['time']:.2f} ms")
    print(f"Total de pedidos cargados: {result['total_orders']}")

    headers = ["Order_ID", "Product", "Country", "Channel",
               "Order_Date", "Price_per_Box", "Amount"]

    print("\nPedido de menor monto:")
    print(tabulate([extract_report_fields(result['min_order'])],
                    headers=headers, tablefmt="fancy_grid"))

    print("\nPedido de mayor monto:")
    print(tabulate([extract_report_fields(result['max_order'])],
                    headers=headers, tablefmt="fancy_grid"))

    print("\nPrimeros 5 registros cargados:")
    rows = [extract_report_fields(o) for o in result['first_five']]
    print(tabulate(rows, headers=headers, tablefmt="fancy_grid"))

    print("\nÚltimos 5 registros cargados:")
    rows = [extract_report_fields(o) for o in result['last_five']]
    print(tabulate(rows, headers=headers, tablefmt="fancy_grid"))

    return result


def extract_report_fields(order):
    """
    Extrae, en el orden correcto, los campos que se deben reportar
    de un pedido para las tablas de la Parte 2.
    """
    return [order['Order_ID'], order['Product'], order['Country'],
            order['Channel'], order['Order_Date'],
            order['Price_per_Box'], order['Amount']]


def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    #TODO: Realizar la función para imprimir un elemento
    pass

def print_req_1(control):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 1
    pass


def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    pass


def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    pass


def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
    pass


def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    pass


def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    pass

# Se crea la lógica asociado a la vista
control = new_logic()

# main del ejercicio
def main():
    """
    Menu principal
    """
    working = True
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        if int(inputs) == 0:
            print("Cargando información de los archivos ....\n")
            data = load_data(control)
        elif int(inputs) == 1:
            print_req_1(control)

        elif int(inputs) == 2:
            print_req_2(control)

        elif int(inputs) == 3:
            print_req_3(control)

        elif int(inputs) == 4:
            print_req_4(control)

        elif int(inputs) == 5:
            print_req_5(control)

        elif int(inputs) == 6:
            print_req_6(control)

        elif int(inputs) == 7:
            working = False
            print("\nGracias por utilizar el programa") 
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)