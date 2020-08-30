def add_one(arr):
    """
    :param: arr - list of digits representing some number x
    return a list with digits represengint (x + 1)
    """
    new_arr = list(reversed(arr.copy()))
    carry = 1
    for i in range(0,len(arr)) : 
        if (carry == 1) :
            if(new_arr[i] == 9) :
                new_arr[i] = 0
                carry =1
            else :
                new_arr[i] += 1
                carry = 0
            
        if(carry == 1 and i == len(arr)-1) :
            new_arr.append(1)
    
    return list(reversed(new_arr))