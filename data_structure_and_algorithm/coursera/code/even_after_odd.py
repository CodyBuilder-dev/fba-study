def even_after_odd(head):
    """
    :param - head - head of linked list
    return - updated list with all even elements are odd elements
    """
    pointer = head
    first_even = None
    last_even = None
    last_even = None
    last_odd = None

    if(head.data %2 == 0) :
        first_even = head
        last_even = first_even
    else :
        first_odd = head
        last_odd = first_odd
        

    while pointer.next :
        print(id(pointer))
        
        print(pointer.data)

        if pointer.data %2 == 0 :
            if first_even is None :
                first_even = pointer
                last_even = pointer
            last_even.next = pointer
            last_even = pointer
            print(id(last_even))
            pointer = last_even.next
            print(id(pointer))
        else :
            if first_odd is None :
                first_odd = pointer
                last_odd = pointer
            last_odd.next = pointer
            last_odd = pointer
            print(id(last_odd))
            pointer = last_odd.next
            print(id(pointer))
    last_odd.next = first_even
