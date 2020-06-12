def recursive_binary_search(target,source,left =0) :
    if len(source) == 0 :
        return None
    center = (len(source)-1) //2
    if source[center] == target :
        return center + left
    elif source[center] < target :
        return recursive_binary_search(target,source[center+1:],left+center+1)
    else :
        return recursive_binary_search(target, source[:center-1],left)

# 처음 발견지점으로부터 선형탐색 사용
def find_first(target, source):
    index = recursive_binary_search(target, source)
    if not index:
        return None
    while source[index] == target:
        if index == 0:
            return 0
        if source[index-1] == target:
            index -= 1
        else:
            return index
multiple = [1, 3, 5, 7, 7, 7, 8, 11, 12, 13, 14, 15]
print(find_first(7, multiple)) # Should return 3
print(find_first(9, multiple)) # Should return None

# 처음 발견지점으로부터 이진탐색 사용
def find_first_target(target,source) :
    
    answer = recursive_binary_search(target,source)
    while answer != None :
        temp_answer = recursive_binary_search(target,source[:answer])
        if temp_answer == None : 
            break
        else : 
            answer = temp_answer
    
    return answer

multiple = [1, 3, 5, 7, 7, 7, 8, 11, 12, 13, 14, 15]
print(find_first_target(7, multiple)) # Should return 3
print(find_first_target(9, multiple)) # Should return None

input_list = [0, 1, 2, 3, 3, 3, 3, 4, 5, 6]
number = 3
print(find_first_target(number, input_list)) # Should return 3

