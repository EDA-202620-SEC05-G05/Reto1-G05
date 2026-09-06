def new_list():
    newlist = {
        "first": None,
        "last": None,
        "size": 0,
    }

    return newlist

def get_element(my_list, pos):
    searchpos = 0
    node = my_list["first"]
    while searchpos < pos:
        node = node["next"]
        searchpos += 1
    return node["info"]

def is_present(my_list, element, cmp_function):
    is_in_array = False
    temp = my_list["first"]
    count = 0
    while not is_in_array and temp is not None:
        if cmp_function(element, temp["info"]) == 0:
            is_in_array = True
        else:
            temp = temp["next"]
            count += 1

    if not is_in_array:
        count = -1
        
    return count

def add_first(my_list, element):
    new_node = {
        "info": element,
        "next": my_list["first"]
    }
    my_list["first"] = new_node
    if my_list["size"] == 0:
        my_list["last"] = new_node
    my_list["size"] += 1
    return 0

def add_last(my_list, element):
    new_node = {
        "info": element,
        "next": None
    }
    if my_list["size"] == 0:
        my_list["first"] = new_node
    else:
        my_list["last"]["next"] = new_node
    my_list["last"] = new_node
    my_list["size"] += 1
    return my_list["size"] - 1

def size(my_list):
    return my_list["size"]

def first_element(my_list):
    if my_list["size"] == 0:
        return None
    return my_list["first"]["info"]
def last_element(my_list):
    if my_list["size"] == 0:
        return None
    return my_list["last"]["info"]

def is_empty(my_list):
    return my_list["size"] == 0
def delete_element(my_list, pos):
    if pos == 0:
        my_list["first"] = my_list["first"]["next"]
        if my_list["size"] == 1:
            my_list["last"] = None
    else:
        prev_node = my_list["first"]
        for _ in range(pos - 1):
            prev_node = prev_node["next"]
        prev_node["next"] = prev_node["next"]["next"]
        if pos == my_list["size"] - 1:
            my_list["last"] = prev_node
    my_list["size"] -= 1
    return my_list
def insert_element(my_list, element, pos):
    if pos == 0:
        add_first(my_list, element)
    elif pos == my_list["size"]:
        add_last(my_list, element)
    else:
        new_node = {
            "info": element,
            "next": None
        }
        prev_node = my_list["first"]
        for _ in range(pos - 1):
            prev_node = prev_node["next"]
        new_node["next"] = prev_node["next"]
        prev_node["next"] = new_node
        my_list["size"] += 1
    return my_list
def change_info(my_list, pos, element):
    node = my_list["first"]
    for _ in range(pos):
        node = node["next"]
    node["info"] = element
    return my_list
def exchange(my_list, pos1, pos2):
    if pos1 == pos2:
        return my_list

    node1 = my_list["first"]
    for _ in range(pos1):
        node1 = node1["next"]

    node2 = my_list["first"]
    for _ in range(pos2):
        node2 = node2["next"]

    node1["info"], node2["info"] = node2["info"], node1["info"]
    return my_list

def sub_list(my_list, pos, num_elements):
    if pos < 0 or pos >= my_list["size"] or num_elements < 0:
        return None
 
    new_sub_list = {
        "first": None,
        "last": None,
        "size": 0,
    }
 
    current_node = my_list["first"]
    for _ in range(pos):
        current_node = current_node["next"]
 
    for _ in range(num_elements):
        if current_node is None:
            break
        add_last(new_sub_list, current_node["info"])
        current_node = current_node["next"]
 
    return new_sub_list
def remove_first(my_list):
    if my_list["size"] == 0:
        return None
    removed_info = my_list["first"]["info"]
    my_list["first"] = my_list["first"]["next"]
    if my_list["size"] == 1:
        my_list["last"] = None
    my_list["size"] -= 1
    return removed_info
def remove_last(my_list):
    if my_list["size"] == 0:
        return None
    if my_list["size"] == 1:
        removed_info = my_list["first"]["info"]
        my_list["first"] = None
        my_list["last"] = None
        my_list["size"] -= 1
        return removed_info

    current_node = my_list["first"]
    while current_node["next"] != my_list["last"]:
        current_node = current_node["next"]

    removed_info = my_list["last"]["info"]
    current_node["next"] = None
    my_list["last"] = current_node
    my_list["size"] -= 1
    return removed_info
 