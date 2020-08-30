# Priority Queue 
# 삽입/삭제 메소드
# Front/Size/Is_empty 멤버

# Priority Queue (Using Arrays)
# O(N)

# Priority Queue (Using Linked Lisk)
# O(N)

# Priority Queue (Using Linked Lisk)
# O(N)

# Priority Queue (Using Hash Map)
# O(N)

# Priority Queue (Using Balanced BST)
# (Balanced 사용 이유 : 양쪽의 높이가 균일해야지만 h = log(N)으로 안전하게 치환 가능)
# (Balanced 되어있지 않은 경우 : 최악의 경우 Linked List와 동일해지므로, O(N) )
# O(log(N))

# Priority Queue (Using Heap)
# (Complete Binary Tree라는 Heap의 조건 때문에, 자동으로 Balanced된다)

# Heap (Using Array)
# 부모 n의 자식은 = 2n + 1 , 2n + 2
# 자식 n의 부모는 = n-1 // 2 
class Heap:
    def __init__(self, initial_size):
        self.cbt = [None for _ in range(initial_size)]        # initialize arrays
        self.next_index = 0                                   # denotes next index where new element should go

    def insert(self, data):
        self.cbt.insert(self.next_index,data)
        self.next_index += 1

        current_index = self.next_index-1
        parent_index = (current_index -1) //2 

        while parent_index >= 0 :
            if self.cbt[parent_index] < self.cbt[current_index] :
                break
            else :
                temp = self.cbt[parent_index]
                self.cbt[parent_index] = self.cbt[current_index]
                self.cbt[current_index] = temp
                current_index = parent_index
                parent_index = (current_index -1) //2 

    
    def remove(self):
        minima = self.cbt[0]
        self.next_index -= 1
        self.cbt[0] = self.cbt[self.next_index]
        self.cbt[self.next_index] = None
        
        current_index = 0
    
        while current_index <= self.next_index : #탈출조건 필요
            left_child_index = current_index*2+1
            right_child_index = current_index*2+2
            left_child = None
            right_child = None

            if self.cbt[left_child_index] is not None :
                left_child = self.cbt[left_child_index]
            if self.cbt[right_child_index] is not None :
                right_child = self.cbt[right_child_index]
            
            if left_child is None :
                break
            else :
                if right_child is None :
                    if self.cbt[current_index] < self.cbt[left_child_index] :
                        temp = self.cbt[left_child_index]
                        self.cbt[left_child_index] = self.cbt[current_index]
                        self.cbt[current_index] = temp
                        current_index = left_child_index
                        left_child_index = current_index*2+1
                        right_child_index = current_index*2+2
                else : 
                    if self.cbt[current_index] < self.cbt[left_child_index] :
                        temp = self.cbt[left_child_index]
                        self.cbt[left_child_index] = self.cbt[current_index]
                        self.cbt[current_index] = temp
                        current_index = left_child_index
                        left_child_index = current_index*2+1
                        right_child_index = current_index*2+2
                    elif self.cbt[current_index] < self.cbt[right_child_index] :
                        temp = self.cbt[right_child_index]
                        self.cbt[right_child_index] = self.cbt[current_index]
                        self.cbt[current_index] = temp
                        current_index = right_child_index
                        left_child_index = current_index*2+1
                        right_child_index = current_index*2+2
                    else : break
            
        return minima
    def size(self) :
        return self.next_index

heap_size = 5
heap = Heap(heap_size)

elements = [1, 2, 3, 4, 1, 2]
for element in elements:
    heap.insert(element)
print('Inserted elements: {}'.format(elements))
    
print('size of heap: {}'.format(heap.size()))

for _ in range(4):
    print('Call remove: {}'.format(heap.remove()))

print('Call get_minimum: {}'.format(heap.get_minimum()))

for _ in range(2):
    print('Call remove: {}'.format(heap.remove()))

print('size of heap: {}'.format(heap.size()))
print('Call remove: {}'.format(heap.remove()))
print('Call is_empty: {}'.format(heap.is_empty()))


# Heap (Using Complete Binary Tree)

