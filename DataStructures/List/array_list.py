def new_list():
    newlist = {
        'elements' : [],
        'size' : 0,
    }
    return newlist 

def get_element(my_list, index):
    return my_list["elements"][index]

def is_present(my_list, element, cmp_function):

    size = my_list["size"]
    if size > 0:
        keyexist = False
        for keypos in range(0, size):
            info = my_list["elements"][keypos]
            if cmp_function(element, info) == 0:
                keyexist = True
                break
        if keyexist:
            return keypos
    return -1 

def add_last(my_list, element):
    my_list['elements'].append(element)
    my_list['size'] += 1
    return my_list['size'] - 1


def size(my_list):
    return my_list['size']

def first_element(my_list):
    if my_list['size'] == 0:
        return None
    return my_list['elements'][0]
def is_empty(my_list):
    return my_list["size"] == 0

def delete_element(my_list, index):
    my_list["elements"].pop(index)
    my_list["size"] -= 1
    return my_list
def insert_element(my_list, index, element):
    my_list["elements"].insert(index, element)
    my_list["size"] += 1
    return my_list
def change_info(my_list, index, element):
    my_list["elements"][index] = element
    return my_list

def size(my_list):
    return my_list["size"]
def last_element(my_list):
    if my_list['size'] == 0:
        return None
    return my_list['elements'][my_list['size'] - 1]

def remove_first(my_list):
    if my_list['size'] == 0:
        return None
    first_element = my_list['elements'][0]
    my_list['elements'].pop(0)
    my_list['size'] -= 1
    return first_element
def remove_last(my_list):
    if my_list['size'] == 0:
        return None
    last_element = my_list['elements'][my_list['size'] - 1]
    my_list['elements'].pop(my_list['size'] - 1)
    my_list['size'] -= 1
    return last_element
def insert_element(my_list, pos, element):
    my_list["elements"].insert(pos, element)
    my_list["size"] += 1
    return my_list

def change_info(my_list, pos, element):
    my_list["elements"][pos] = element
    return my_list
def exchange_elements(my_list, pos1, pos2):
    my_list["elements"][pos1], my_list["elements"][pos2] = my_list["elements"][pos2], my_list["elements"][pos1]
    return my_list
def sub_list(my_list, pos, num_elements):
    sublist = {
        'elements': my_list['elements'][pos:pos + num_elements],
        'size': num_elements,
    }
    return sublist
