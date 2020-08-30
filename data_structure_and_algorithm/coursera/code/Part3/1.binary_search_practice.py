def binary_search(array,target) :
    if len(array) == 0 : return -1

    left = 0
    right = len(array)-1
    #middle = int((left + right)/2)
    middle = (left+right)//2

    while array[middle] != target :
        if(right <= left) : return -1

        if array[middle] >= target :
            right = middle - 1
        else : 
            left = middle + 1
        

        #middle = int((left + right)/2)
        middle = (left+right)//2

    return middle


case_a = [1,4,6,9,10]

for i in range(100) :
    print(binary_search(case_a,i))

case_b = []
binary_search(case_b,10)