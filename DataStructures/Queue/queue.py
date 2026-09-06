from DataStructures.List import array_list as lt

def new_queue():
    return lt.new_list()

def enqueue(queue, element):
    lt.add_last(queue, element)

def dequeue(queue):
    if lt.is_empty(queue):
        return None
    return lt.remove_first(queue)

def is_empty(queue):
    return lt.is_empty(queue)

def peek(queue):
    if lt.is_empty(queue):
        return None
    return lt.get_element(queue, 0)

def size(queue):
    return lt.size(queue)