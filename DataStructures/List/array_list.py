def new_list():
    """
    Crea una lista (array_list) vacía.
    """
    my_list = {
        'elements': [],
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
    my_list['elements'].insert(0, element)
    my_list['size'] += 1
    return my_list
 
 
def add_last(my_list, element):
    """
    Agrega un elemento al final de la lista.
    """
    my_list['elements'].append(element)
    my_list['size'] += 1
    return my_list
 
 
def first_element(my_list):
    """
    Retorna el primer elemento de la lista (sin eliminarlo).
    """
    if is_empty(my_list):
        raise Exception('IndexError: list index out of range')
    return my_list['elements'][0]
 
 
def last_element(my_list):
    """
    Retorna el último elemento de la lista (sin eliminarlo).
    """
    if is_empty(my_list):
        raise Exception('IndexError: list index out of range')
    return my_list['elements'][my_list['size'] - 1]
 
 
def get_element(my_list, pos):
    """
    Retorna el elemento en la posición dada (sin eliminarlo).
    """
    if pos < 0 or pos >= my_list['size']:
        raise Exception('IndexError: list index out of range')
    return my_list['elements'][pos]
 
 
def delete_element(my_list, pos):
    """
    Elimina el elemento en la posición dada.
    """
    if pos < 0 or pos >= my_list['size']:
        raise Exception('IndexError: list index out of range')
    my_list['elements'].pop(pos)
    my_list['size'] -= 1
    return my_list
 
 
def remove_first(my_list):
    """
    Elimina y retorna el primer elemento de la lista.
    """
    if is_empty(my_list):
        raise Exception('IndexError: list index out of range')
    removed = my_list['elements'].pop(0)
    my_list['size'] -= 1
    return removed
 
 
def remove_last(my_list):
    """
    Elimina y retorna el último elemento de la lista.
    """
    if is_empty(my_list):
        raise Exception('IndexError: list index out of range')
    removed = my_list['elements'].pop(my_list['size'] - 1)
    my_list['size'] -= 1
    return removed
 
 
def insert_element(my_list, element, pos):
    """
    Inserta un elemento en la posición dada.
    """
    my_list['elements'].insert(pos, element)
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
    for pos in range(my_list['size']):
        info = my_list['elements'][pos]
        if cmp_function(element, info) == 0:
            return pos
    return -1
 
 
def change_info(my_list, pos, new_info):
    """
    Cambia la información del elemento en la posición dada.
    """
    if pos < 0 or pos >= my_list['size']:
        raise Exception('IndexError: list index out of range')
    my_list['elements'][pos] = new_info
    return my_list
 
 
def exchange(my_list, pos_1, pos_2):
    """
    Intercambia la información de los elementos en las posiciones dadas.
    """
    my_list['elements'][pos_1], my_list['elements'][pos_2] = \
        my_list['elements'][pos_2], my_list['elements'][pos_1]
    return my_list
 
 
def sub_list(my_list, pos_i, num_elements):
    """
    Retorna una sublista que inicia en pos_i y contiene num_elements elementos.
    """
    if pos_i < 0 or pos_i >= my_list['size']:
        raise Exception('IndexError: list index out of range')
    sublist = {
        'elements': my_list['elements'][pos_i: pos_i + num_elements],
        'size': len(my_list['elements'][pos_i: pos_i + num_elements]),
    }
    return sublist
 
 
def to_py_list(my_list):
    """
    Retorna los elementos de la lista en una lista nativa de Python.
    """
    return my_list['elements']