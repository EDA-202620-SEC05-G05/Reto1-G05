def new_list():
    """
    Crea una lista (single_linked_list) vacía.
    """
    my_list = {
        'first': None,
        'last': None,
        'size': 0,
    }
    return my_list
 
 
def is_empty(my_list):
    """
    Retorna True si la lista está vacía, False en caso contrario.
    """
    return my_list['size'] == 0
 
 
def size(my_list):
    """
    Retorna el tamaño de la lista.
    """
    return my_list['size']
 
 
def add_first(my_list, element):
    """
    Agrega un elemento al inicio de la lista.
    """
    new_node = {
        'info': element,
        'next': my_list['first']
    }
    my_list['first'] = new_node
    if my_list['size'] == 0:
        my_list['last'] = new_node
    my_list['size'] += 1
    return my_list
 
 
def add_last(my_list, element):
    """
    Agrega un elemento al final de la lista.
    """
    new_node = {
        'info': element,
        'next': None
    }
    if my_list['size'] == 0:
        my_list['first'] = new_node
    else:
        my_list['last']['next'] = new_node
    my_list['last'] = new_node
    my_list['size'] += 1
    return my_list
 
 
def first_element(my_list):
    """
    Retorna el primer elemento de la lista (sin eliminarlo).
    """
    if is_empty(my_list):
        raise Exception('IndexError: list index out of range')
    return my_list['first']['info']
 
 
def last_element(my_list):
    """
    Retorna el último elemento de la lista (sin eliminarlo).
    """
    if is_empty(my_list):
        raise Exception('IndexError: list index out of range')
    return my_list['last']['info']
 
 
def get_element(my_list, pos):
    """
    Retorna el elemento en la posición dada (sin eliminarlo).
    """
    if pos < 0 or pos >= my_list['size']:
        raise Exception('IndexError: list index out of range')
    node = my_list['first']
    for _ in range(pos):
        node = node['next']
    return node['info']
 
 
def delete_element(my_list, pos):
    """
    Elimina el elemento en la posición dada.
    """
    if pos < 0 or pos >= my_list['size']:
        raise Exception('IndexError: list index out of range')
 
    if pos == 0:
        my_list['first'] = my_list['first']['next']
        if my_list['size'] == 1:
            my_list['last'] = None
    else:
        prev_node = my_list['first']
        for _ in range(pos - 1):
            prev_node = prev_node['next']
        prev_node['next'] = prev_node['next']['next']
        if pos == my_list['size'] - 1:
            my_list['last'] = prev_node
 
    my_list['size'] -= 1
    return my_list
 
 
def remove_first(my_list):
    """
    Elimina y retorna el primer elemento de la lista.
    """
    if is_empty(my_list):
        raise Exception('IndexError: list index out of range')
    removed_info = my_list['first']['info']
    my_list['first'] = my_list['first']['next']
    if my_list['size'] == 1:
        my_list['last'] = None
    my_list['size'] -= 1
    return removed_info
 
 
def remove_last(my_list):
    """
    Elimina y retorna el último elemento de la lista.
    """
    if is_empty(my_list):
        raise Exception('IndexError: list index out of range')
 
    if my_list['size'] == 1:
        removed_info = my_list['first']['info']
        my_list['first'] = None
        my_list['last'] = None
        my_list['size'] -= 1
        return removed_info
 
    current_node = my_list['first']
    while current_node['next'] != my_list['last']:
        current_node = current_node['next']
 
    removed_info = my_list['last']['info']
    current_node['next'] = None
    my_list['last'] = current_node
    my_list['size'] -= 1
    return removed_info
 
 
def insert_element(my_list, element, pos):
    """
    Inserta un elemento en la posición dada (0 <= pos <= size(my_list)).
    """
    if pos < 0 or pos > my_list['size']:
        raise Exception('IndexError: list index out of range')
 
    if pos == 0:
        add_first(my_list, element)
    elif pos == my_list['size']:
        add_last(my_list, element)
    else:
        new_node = {
            'info': element,
            'next': None
        }
        prev_node = my_list['first']
        for _ in range(pos - 1):
            prev_node = prev_node['next']
        new_node['next'] = prev_node['next']
        prev_node['next'] = new_node
        my_list['size'] += 1
    return my_list
 
 
def default_function(element_1, element_2):
    """
    Función de comparación por defecto (a modo de ejemplo).
    """
    if element_1 > element_2:
        return 1
    elif element_1 < element_2:
        return -1
    return 0
 
 
def is_present(my_list, element, cmp_function):
    """
    Retorna la posición del elemento si está presente en la lista
    (usando cmp_function para comparar), o -1 si no está presente.
    """
    temp = my_list['first']
    pos = 0
    while temp is not None:
        if cmp_function(element, temp['info']) == 0:
            return pos
        temp = temp['next']
        pos += 1
    return -1
 
 
def change_info(my_list, pos, new_info):
    """
    Cambia la información del elemento en la posición dada.
    """
    if pos < 0 or pos >= my_list['size']:
        raise Exception('IndexError: list index out of range')
    node = my_list['first']
    for _ in range(pos):
        node = node['next']
    node['info'] = new_info
    return my_list
 
 
def exchange(my_list, pos_1, pos_2):
    """
    Intercambia la información de los elementos en las posiciones dadas.
    """
    if (pos_1 < 0 or pos_1 >= my_list['size'] or
            pos_2 < 0 or pos_2 >= my_list['size']):
        raise Exception('IndexError: list index out of range')
 
    if pos_1 == pos_2:
        return my_list
 
    node_1 = my_list['first']
    for _ in range(pos_1):
        node_1 = node_1['next']
 
    node_2 = my_list['first']
    for _ in range(pos_2):
        node_2 = node_2['next']
 
    node_1['info'], node_2['info'] = node_2['info'], node_1['info']
    return my_list
 
 
def sub_list(my_list, pos, num_elements):
    """
    Retorna una sublista que contiene num_elements elementos a partir
    de la posición pos.
    """
    if pos < 0 or pos >= my_list['size']:
        raise Exception('IndexError: list index out of range')
 
    new_sub_list = new_list()
 
    current_node = my_list['first']
    for _ in range(pos):
        current_node = current_node['next']
 
    for _ in range(num_elements):
        if current_node is None:
            break
        add_last(new_sub_list, current_node['info'])
        current_node = current_node['next']
 
    return new_sub_list
 
 
def adjacents(my_list, element):
    """
    Retorna una lista de Python con el elemento siguiente al elemento
    dado (si existe). Si el elemento dado no existe, retorna None.
    """
    current_node = my_list['first']
    while current_node is not None:
        if current_node['info'] == element:
            if current_node['next'] is not None:
                return [current_node['next']['info']]
            return []
        current_node = current_node['next']
    return None
 
 
def to_py_list(my_list):
    """
    Retorna los elementos de la lista (en orden) en una lista de Python.
    """
    result = []
    current_node = my_list['first']
    while current_node is not None:
        result.append(current_node['info'])
        current_node = current_node['next']
    return result