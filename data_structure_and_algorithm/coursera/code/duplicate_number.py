def duplicate_number(arr):
    """
    :param - array containing numbers in the range [0, len(arr) - 2]
    return - the number that is duplicate in the arr
    """
    count = [0]*len(arr)
    for i in arr :
        if count[i] == 0 :
            count[i] +=1
        else :
            return i