import time
import csv
from DataStructures.List import array_list as lt
from DataStructures.List import single_linked_list as sll

#recomendacion
csv.field_size_limit(2147483647)

def new_logic():
    """
    Crea el catalogo para almacenar las estructuras de datos
    """
    catalog = {
        'orders': lt.new_list()   # lista que almacena cada pedido
    }
    return catalog


# Funciones para la carga de datos


def load_data(catalog, filename):
    """
    Carga los datos del reto
    """
    start_time = get_time()

    with open(filename, encoding='utf-8') as csv_file:
        input_file = csv.DictReader(csv_file)
        for row in input_file:
            order = format_order(row)
            catalog['orders'] = lt.add_last(catalog['orders'], order)

    end_time = get_time()
    total_time = delta_time(start_time, end_time)

    total_orders = lt.size(catalog['orders'])
    min_order, max_order = find_min_max_amount(catalog['orders'])
    first_five, last_five = get_first_last(catalog['orders'])

    return {
        'time': total_time,
        'total_orders': total_orders,
        'min_order': min_order,
        'max_order': max_order,
        'first_five': first_five,
        'last_five': last_five
    }


def format_order(row):
    """
    Convierte una fila cruda del CSV (todo strings) en un dict con los
    tipos correctos, reemplazando los vacíos por 'Unknown'.
    """
    def to_float(value):
        return float(value) if value not in (None, '') else 'Unknown'

    def to_int(value):
        return int(value) if value not in (None, '') else 'Unknown'

    def to_str(value):
        return value if value not in (None, '') else 'Unknown'

    order = {
        'Order_ID': to_str(row.get('Order_ID')),
        'Product': to_str(row.get('Product')),
        'Country': to_str(row.get('Country')),
        'Channel': to_str(row.get('Channel')),
        'Order_Date': to_str(row.get('Order_Date')),
        'Discount_Pct': to_float(row.get('Discount_Pct')),
        'Price_per_Box': to_float(row.get('Price_per_Box')),
        'Marketing_Spend': to_float(row.get('Marketing_Spend')),
        'Boxes_Shipped': to_int(row.get('Boxes_Shipped')),
        'Amount': to_float(row.get('Amount'))
    }
    return order


def find_min_max_amount(orders):
    """
    Recorre el array_list UNA vez y encuentra el pedido de menor y de mayor
    Amount. Si hay empate en Amount, gana el de menor Price_per_Box.
    """
    min_order = None
    max_order = None

    for i in range(lt.size(orders)):
        order = lt.get_element(orders, i)

        if order['Amount'] == 'Unknown':
            continue  # no se puede comparar un Amount desconocido

        if min_order is None:
            min_order = order
            max_order = order
            continue

        if (order['Amount'] < min_order['Amount'] or
                (order['Amount'] == min_order['Amount'] and
                 order['Price_per_Box'] < min_order['Price_per_Box'])):
            min_order = order

        if (order['Amount'] > max_order['Amount'] or
                (order['Amount'] == max_order['Amount'] and
                 order['Price_per_Box'] < max_order['Price_per_Box'])):
            max_order = order

    return min_order, max_order


def get_first_last(orders):
    """
    Retorna (como listas de Python) los primeros 5 y los últimos 5
    pedidos cargados, en el orden en que aparecen en el archivo.
    """
    total = lt.size(orders)
    n = min(5, total)

    first_sub = lt.sub_list(orders, 0, n)
    last_sub = lt.sub_list(orders, max(0, total - n), n)

    return lt.to_py_list(first_sub), lt.to_py_list(last_sub) 

# Funciones de consulta sobre el catálogo


def req_1(catalog):
    """
    Retorna el resultado del requerimiento 1
    """
    # TODO: Modificar el requerimiento 1
    pass


def req_2(catalog):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    pass


def req_3(catalog):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    pass


def req_4(catalog):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    pass


def req_5(catalog):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    pass

def req_6(catalog):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    pass


# Funciones para medir tiempos de ejecucion

def get_time():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def delta_time(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed
