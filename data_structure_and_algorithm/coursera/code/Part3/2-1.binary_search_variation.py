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

# Test Code
case_a = [1,4,6,9,10]

print("테스트 케이스 A")
for i in range(100) :
    print(recursive_binary_search(i,case_a))


case_b = []
print("테스트 케이스 B")
print(recursive_binary_search(10,case_b))


multiple = [1, 3, 5, 7, 7, 7, 8, 11, 12]
print("테스트 케이스 multiple")
print(recursive_binary_search(7,multiple))