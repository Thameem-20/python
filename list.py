def add_to_list(my_list, item):
    if len(my_list) < 10:
        my_list.append(item) 
    else:
        print("List is already at maximum capacity (10 items).")
    
    return my_list  
