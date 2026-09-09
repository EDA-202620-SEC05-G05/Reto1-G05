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

def extraer_campos_pedido(pedido):
    """
    Extrae Product, Country, Channel, Order_Date, Price_per_Box y Amount
    de un pedido, en ese orden, para las tablas de los requerimientos.
    """
    return [pedido['Product'], pedido['Country'], pedido['Channel'],
            pedido['Order_Date'], pedido['Price_per_Box'], pedido['Amount']]


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
    precio_min = float(input("Ingrese el precio mínimo por caja: "))
    precio_max = float(input("Ingrese el precio máximo por caja: "))

    resultado = logic.req_2(control, precio_min, precio_max)

    print(f"\nTiempo de ejecución: {resultado['time']:.2f} ms")
    print(f"Cantidad de pedidos en el rango: {resultado['total']}")
    print(f"Promedio Discount_Pct: {resultado['avg_discount']:.2f}")
    print(f"Promedio Marketing_Spend: {resultado['avg_marketing']:.2f}")
    print(f"Promedio Price_per_Box: {resultado['avg_price']:.2f}")

    headers = ["Product", "Country", "Channel", "Order_Date",
               "Price_per_Box", "Amount"]

    print("\nPedido más reciente del rango:")
    print(tabulate([extraer_campos_pedido(resultado['most_recent'])],
                    headers=headers, tablefmt="fancy_grid"))

    print("\nPedido de menor Amount en el rango:")
    print(tabulate([extraer_campos_pedido(resultado['min_amount_order'])],
                    headers=headers, tablefmt="fancy_grid"))

    print("\nPedido de mayor Amount en el rango:")
    print(tabulate([extraer_campos_pedido(resultado['max_amount_order'])],
                    headers=headers, tablefmt="fancy_grid"))


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
    producto = input("Ingrese el nombre del producto: ")
    pais = input("Ingrese el país: ")

    resultado = logic.req_4(control, producto, pais)

    print(f"\nTiempo de ejecución: {resultado['time']:.2f} ms")
    print(f"Cantidad de pedidos que cumplen el filtro: {resultado['total']}")
    print(f"Precio promedio (Price_per_Box): {resultado['avg_price']:.2f}")
    print(f"Promedio Discount_Pct: {resultado['avg_discount']:.2f}")
    print(f"Promedio Marketing_Spend: {resultado['avg_marketing']:.2f}")
    print(f"Promedio Boxes_Shipped: {resultado['avg_boxes']:.2f}")

    headers = ["Order_ID", "Channel", "Order_Date", "Boxes_Shipped", "Amount"]

    def campos_req4(pedido):
        return [pedido['Order_ID'], pedido['Channel'], pedido['Order_Date'],
                pedido['Boxes_Shipped'], pedido['Amount']]

    print("\nLos 2 pedidos de mayor Amount:")
    filas = [campos_req4(resultado['top_1']), campos_req4(resultado['top_2'])]
    print(tabulate(filas, headers=headers, tablefmt="fancy_grid"))


def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    filtro = input("Ingrese el filtro (MENOR o MAYOR): ").strip().upper()
    producto = input("Ingrese el nombre del producto: ")
    fecha_inicial = input("Ingrese la fecha inicial (YYYY-MM-DD): ")
    fecha_final = input("Ingrese la fecha final (YYYY-MM-DD): ")

    resultado = logic.req_5(control, filtro, producto, fecha_inicial, fecha_final)

    print(f"\nTiempo de ejecución: {resultado['time']:.2f} ms")
    print(f"Filtro seleccionado: {resultado['filtro']}")
    print(f"Cantidad de pedidos que cumplen el filtro: {resultado['total']}")

    pedido = resultado['result_order']
    headers = ["Price_per_Box", "Boxes_Shipped", "Amount",
               "Channel", "Order_Date", "Marketing_Spend"]
    fila = [pedido['Price_per_Box'], pedido['Boxes_Shipped'], pedido['Amount'],
            pedido['Channel'], pedido['Order_Date'], pedido['Marketing_Spend']]

    print(f"\nPedido resultante ({resultado['filtro']} Amount):")
    print(tabulate([fila], headers=headers, tablefmt="fancy_grid"))

    print(f"\nPromedio Price_per_Box: {resultado['avg_price']:.2f}")
    print(f"Promedio Boxes_Shipped: {resultado['avg_boxes']:.2f}")
    print(f"Promedio Marketing_Spend: {resultado['avg_marketing']:.2f}")


def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    fecha_inicial = input("Ingrese la fecha inicial (YYYY-MM-DD): ")
    fecha_final = input("Ingrese la fecha final (YYYY-MM-DD): ")

    resultado = logic.req_6(control, fecha_inicial, fecha_final)

    print(f"\nTiempo de ejecución: {resultado['time']:.2f} ms")
    print(f"Total de pedidos en el rango de fechas: {resultado['total_orders']}")

    canal_top_pedidos = resultado['most_used']
    print(f"\nCanal más usado: {canal_top_pedidos['Channel']} "
          f"({canal_top_pedidos['count']} pedidos, "
          f"recaudo total {canal_top_pedidos['total_amount']:.2f})")

    canal_top_recaudo = resultado['most_revenue']
    print(f"Canal que más recauda: {canal_top_recaudo['Channel']} "
          f"({canal_top_recaudo['count']} pedidos, "
          f"recaudo total {canal_top_recaudo['total_amount']:.2f})")

    headers = ["Channel", "Pedidos", "Recaudo total",
               "Precio prom.", "Marketing prom."]
    filas = []
    for canal in resultado['channels']:
        filas.append([canal['Channel'], canal['count'],
                       round(canal['total_amount'], 2),
                       round(canal['avg_price'], 2),
                       round(canal['avg_marketing'], 2)])

    print("\nEstadísticas por canal:")
    print(tabulate(filas, headers=headers, tablefmt="fancy_grid"))

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