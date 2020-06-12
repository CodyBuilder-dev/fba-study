def binary_search(target,source) :
    if len(source) == 0 :
        return -1
    left = 0
    right = len(source) - 1
    
    while left<right :
        middle = (left+right)//2
        if source[middle] == target :
            return middle
        elif source[middle] > target :
            right = middle-1
        else :
            left = middle+1

    return -1

def contains(target,source) :
    index = binary_search(target,source)
    if index == -1 :
        return False
    else :
        return True

letters = ['a', 'c', 'd', 'f', 'g']
print(contains('a', letters)) ## True
print(contains('b', letters)) ## False