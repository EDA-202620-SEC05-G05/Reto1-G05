from DataStructures.List import array_list as lt
 
 
def new_stack():
    return lt.new_list()
 
 
def push(stack, element):
    lt.add_last(stack, element)
 
 
def pop(stack):
    if lt.is_empty(stack):
        return None
    element = lt.last_element(stack)
    lt.remove_last(stack)
    return element
 
 
def is_empty(stack):
    return lt.is_empty(stack)
 
 
def top(stack):
    if lt.is_empty(stack):
        return None
    return lt.last_element(stack)
 
 
def size(stack):
    return lt.size(stack)