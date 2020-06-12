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


def first_and_last_index(source,target): 
    middle_idx = recursive_binary_search(target,source)
    if middle_idx == None : return None

    temp_middle_idx = middle_idx
    # find first_idx
    while temp_middle_idx != None :
        temp_answer = recursive_binary_search(target,source[:temp_middle_idx-1])
        if temp_answer == None : 
            break
        else : 
            temp_middle_idx = temp_answer

    first_idx = temp_middle_idx
   
    temp_middle_idx = middle_idx
    # find last_idx
    while temp_middle_idx != None :
        temp_answer = recursive_binary_search(target,source[temp_middle_idx+1:])
        if temp_answer == None : 
            break
        else : 
            temp_middle_idx = temp_answer

    last_idx = temp_middle_idx

    return [first_idx,last_idx]

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    solution = test_case[2]
    output = first_and_last_index(input_list, number)
    if output == solution:
        print("Pass")
    else:
        print("Fail")

input_list = [1]
number = 1
solution = [0, 0]
test_case_1 = [input_list, number, solution]
test_function(test_case_1)

input_list = [0, 1, 2, 3, 3, 3, 3, 4, 5, 6]
number = 3
solution = [3, 6]
test_case_2 = [input_list, number, solution]
test_function(test_case_2)

input_list = [0, 1, 2, 3, 4, 5]
number = 5
solution = [5, 5]
test_case_3 = [input_list, number, solution]
test_function(test_case_3)

input_list = [0, 1, 2, 3, 4, 5]
number = 6
solution = [-1, -1]
test_case_4 = [input_list, number, solution]
test_function(test_case_4)

    
    