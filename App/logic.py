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

    with open(filename, encoding='utf-8-sig') as csv_file:
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


def req_1(catalog, product_name):
    """
    Retorna el resultado del requerimiento 1: estadisticas promedio de
    todos los pedidos de un producto dado.
    """
    start_time = get_time()

    orders = catalog['orders']

    total = 0
    sum_price = 0.0
    min_price = None
    max_price = None
    sum_discount = 0.0
    min_discount = None
    max_discount = None
    sum_boxes = 0.0
    min_boxes = None
    max_boxes = None
    sum_marketing = 0.0
    min_marketing = None
    max_marketing = None
    year_counts = {}
    max_amount_order = None
    min_amount_order = None

    for i in range(lt.size(orders)):
        order = lt.get_element(orders, i)

        if order['Product'] != product_name:
            continue

        total += 1

        price = order['Price_per_Box']
        discount = order['Discount_Pct']
        boxes = order['Boxes_Shipped']
        marketing = order['Marketing_Spend']
        amount = order['Amount']
        date = order['Order_Date']

        if price != 'Unknown':
            sum_price += price
            if min_price is None or price < min_price:
                min_price = price
            if max_price is None or price > max_price:
                max_price = price

        if discount != 'Unknown':
            sum_discount += discount
            if min_discount is None or discount < min_discount:
                min_discount = discount
            if max_discount is None or discount > max_discount:
                max_discount = discount

        if boxes != 'Unknown':
            sum_boxes += boxes
            if min_boxes is None or boxes < min_boxes:
                min_boxes = boxes
            if max_boxes is None or boxes > max_boxes:
                max_boxes = boxes

        if marketing != 'Unknown':
            sum_marketing += marketing
            if min_marketing is None or marketing < min_marketing:
                min_marketing = marketing
            if max_marketing is None or marketing > max_marketing:
                max_marketing = marketing

        if date != 'Unknown':
            year = date[0:4]
            if year in year_counts:
                year_counts[year] += 1
            else:
                year_counts[year] = 1

        if amount != 'Unknown':
            # Pedido de mayor Amount (empate -> menor Marketing_Spend)
            if max_amount_order is None:
                max_amount_order = order
            elif (amount > max_amount_order['Amount'] or
                    (amount == max_amount_order['Amount'] and
                     marketing != 'Unknown' and
                     max_amount_order['Marketing_Spend'] != 'Unknown' and
                     marketing < max_amount_order['Marketing_Spend'])):
                max_amount_order = order

            # Pedido de menor Amount (empate -> menor Marketing_Spend)
            if min_amount_order is None:
                min_amount_order = order
            elif (amount < min_amount_order['Amount'] or
                    (amount == min_amount_order['Amount'] and
                     marketing != 'Unknown' and
                     min_amount_order['Marketing_Spend'] != 'Unknown' and
                     marketing < min_amount_order['Marketing_Spend'])):
                min_amount_order = order

    end_time = get_time()

    result = {
        'time': delta_time(start_time, end_time),
        'total': total
    }

    if total == 0:
        return result

    top_year = None
    top_year_count = 0
    for year in year_counts:
        if year_counts[year] > top_year_count:
            top_year_count = year_counts[year]
            top_year = year

    result['avg_price'] = sum_price / total
    result['min_price'] = min_price
    result['max_price'] = max_price

    result['avg_discount'] = sum_discount / total
    result['min_discount'] = min_discount
    result['max_discount'] = max_discount

    result['avg_boxes'] = sum_boxes / total
    result['min_boxes'] = min_boxes
    result['max_boxes'] = max_boxes

    result['avg_marketing'] = sum_marketing / total
    result['min_marketing'] = min_marketing
    result['max_marketing'] = max_marketing

    result['top_year'] = top_year
    result['top_year_count'] = top_year_count

    result['max_amount_order'] = max_amount_order
    result['min_amount_order'] = min_amount_order

    return result


def req_2(catalog, min_price, max_price):
    """
    Retorna el resultado del requerimiento 2: filtra pedidos cuyo
    Price_per_Box está entre min_price y max_price (inclusive).
    """
    start_time = get_time()
 
    filtered = lt.new_list()
    sum_discount = 0.0
    sum_marketing = 0.0
    sum_price = 0.0
 
    for i in range(lt.size(catalog['orders'])):
        order = lt.get_element(catalog['orders'], i)
        price = order['Price_per_Box']
        if price == 'Unknown':
            continue
        if min_price <= price <= max_price:
            filtered = lt.add_last(filtered, order)
            sum_discount += order['Discount_Pct']
            sum_marketing += order['Marketing_Spend']
            sum_price += price
 
    total = lt.size(filtered)
 
    avg_discount = sum_discount / total if total > 0 else 0
    avg_marketing = sum_marketing / total if total > 0 else 0
    avg_price = sum_price / total if total > 0 else 0
 
    most_recent = None
    min_amount_order = None
    max_amount_order = None
 
    for i in range(total):
        order = lt.get_element(filtered, i)
 
        # Pedido más reciente (mayor Order_Date pero si empatan el que tenga mayor Amount)
        if most_recent is None:
            most_recent = order
        elif (order['Order_Date'] > most_recent['Order_Date'] or
              (order['Order_Date'] == most_recent['Order_Date'] and
               order['Amount'] > most_recent['Amount'])):
            most_recent = order
 
        # Menor y mayor Amount (si empatan se verifica el menor Price_per_Box)
        if order['Amount'] == 'Unknown':
            continue
        if min_amount_order is None:
            min_amount_order = order
            max_amount_order = order
            continue
        if (order['Amount'] < min_amount_order['Amount'] or
                (order['Amount'] == min_amount_order['Amount'] and
                 order['Price_per_Box'] < min_amount_order['Price_per_Box'])):
            min_amount_order = order
        if (order['Amount'] > max_amount_order['Amount'] or
                (order['Amount'] == max_amount_order['Amount'] and
                 order['Price_per_Box'] < max_amount_order['Price_per_Box'])):
            max_amount_order = order
 
    end_time = get_time()
 
    return {
        'time': delta_time(start_time, end_time),
        'total': total,
        'avg_discount': avg_discount,
        'avg_marketing': avg_marketing,
        'avg_price': avg_price,
        'most_recent': most_recent,
        'min_amount_order': min_amount_order,
        'max_amount_order': max_amount_order,
    }



def req_3(catalog, country, channel):
    """
    Retorna el resultado del requerimiento 3: promedios para pedidos de un
    país y canal específicos.
    """
    start_time = get_time()

    orders = catalog['orders']
    total_orders = lt.size(orders)

    count = 0
    sum_price = 0.0
    sum_discount = 0.0
    sum_marketing = 0.0
    sum_boxes = 0.0

    product_counts = {}
    year_counts = {}

    for i in range(total_orders):
        order = lt.get_element(orders, i)

        if order['Country'] == country and order['Channel'] == channel:
            count += 1

            price = order['Price_per_Box']
            discount = order['Discount_Pct']
            marketing = order['Marketing_Spend']
            boxes = order['Boxes_Shipped']
            product = order['Product']
            date = order['Order_Date']

            if price != 'Unknown':
                sum_price += price
            if discount != 'Unknown':
                sum_discount += discount
            if marketing != 'Unknown':
                sum_marketing += marketing
            if boxes != 'Unknown':
                sum_boxes += boxes

            if product != 'Unknown':
                product_counts[product] = product_counts.get(product, 0) + 1

            if date != 'Unknown' and len(date) >= 4:
                year = date[0:4]
                year_counts[year] = year_counts.get(year, 0) + 1

    end_time = get_time()

    result = {
        'time': delta_time(start_time, end_time),
        'total': count
    }

    if count == 0:
        result['avg_price'] = 0.0
        result['avg_discount'] = 0.0
        result['avg_marketing'] = 0.0
        result['avg_boxes'] = 0.0
        result['most_frequent_product'] = 'Unknown'
        result['year_with_most_orders'] = 'Unknown'
        return result

    most_frequent_product = 'Unknown'
    max_prod_count = 0
    for prod in product_counts:
        if product_counts[prod] > max_prod_count:
            max_prod_count = product_counts[prod]
            most_frequent_product = prod

    year_with_most_orders = 'Unknown'
    max_year_count = 0
    for yr in year_counts:
        if year_counts[yr] > max_year_count:
            max_year_count = year_counts[yr]
            year_with_most_orders = yr

    result['avg_price'] = sum_price / count
    result['avg_discount'] = sum_discount / count
    result['avg_marketing'] = sum_marketing / count
    result['avg_boxes'] = sum_boxes / count
    result['most_frequent_product'] = most_frequent_product
    result['year_with_most_orders'] = year_with_most_orders

    return result

def req_4(catalog, product, country):
    """
    Retorna el resultado del requerimiento 4: precio promedio para la
    combinación Producto-País, y los 2 pedidos de mayor Amount.
    """
    start_time = get_time()
 
    filtered = sll.new_list()
    sum_price = 0.0
    sum_discount = 0.0
    sum_marketing = 0.0
    sum_boxes = 0.0
 
    for i in range(lt.size(catalog['orders'])):
        order = lt.get_element(catalog['orders'], i)
        if order['Product'] == product and order['Country'] == country:
            filtered = sll.add_last(filtered, order)
            sum_price += order['Price_per_Box']
            sum_discount += order['Discount_Pct']
            sum_marketing += order['Marketing_Spend']
            sum_boxes += order['Boxes_Shipped']
 
    total = sll.size(filtered)
    avg_price = sum_price / total if total > 0 else 0
    avg_discount = sum_discount / total if total > 0 else 0
    avg_marketing = sum_marketing / total if total > 0 else 0
    avg_boxes = sum_boxes / total if total > 0 else 0
 
    top_1 = None
    top_2 = None
 
    for i in range(total):
        order = sll.get_element(filtered, i)
        if order['Amount'] == 'Unknown':
            continue
        if es_mejor_monto(order, top_1):
            top_2 = top_1
            top_1 = order
        elif es_mejor_monto(order, top_2):
            top_2 = order
 
    end_time = get_time()
 
    return {
        'time': delta_time(start_time, end_time),
        'total': total,
        'avg_price': avg_price,
        'avg_discount': avg_discount,
        'avg_marketing': avg_marketing,
        'avg_boxes': avg_boxes,
        'top_1': top_1,
        'top_2': top_2,
    }
 
 
def es_mejor_monto(candidate, current_best):
    """
    Retorna True si 'candidate' debe ir antes que 'current_best' según
    el criterio del requerimiento 4: mayor Amount; empate -> menor
    Marketing_Spend; empate -> menor Order_ID.
    """
    if current_best is None:
        return True
    if candidate['Amount'] != current_best['Amount']:
        return candidate['Amount'] > current_best['Amount']
    if candidate['Marketing_Spend'] != current_best['Marketing_Spend']:
        return candidate['Marketing_Spend'] < current_best['Marketing_Spend']
    return candidate['Order_ID'] < current_best['Order_ID']

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
