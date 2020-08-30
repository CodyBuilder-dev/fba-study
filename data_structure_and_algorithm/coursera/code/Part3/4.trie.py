#Simple Trie (using python Dict)
basic_trie = {
    'a' : {
        'd' : {
            'd' :{
                'word_end':True
                },
            'word_end':False
        },
        'word_end' : True
    },
    'h' : {
        'i':{
            'word_end': True
        },
        'word_end':False
    }
}

print('Is "a"   a word: {}'.format(basic_trie['a']['word_end']))
print('Is "ad"  a word: {}'.format(basic_trie['a']['d']['word_end']))
print('Is "add" a word: {}'.format(basic_trie['a']['d']['d']['word_end']))

def is_word(word,trie):
    current_node = trie
    
    for char in word:
        if char not in current_node:
            return False
        else : 
            current_node = current_node[char]

    return current_node['word_end']



test_words = ['hi','ap', 'add']
for word in test_words:
    if is_word(word,basic_trie):
        print('"{}" is a word.'.format(word))
    else:
        print('"{}" is not a word.'.format(word))

# Trie (using Class)
# 삽입 메소드/삭제 메소드/탐색 메소드 3가지 필요
class TrieNode(object):
    def __init__(self):
        self.is_word = False
        self.children = {}

class Trie(object):
    def __init__(self):
        self.root = TrieNode()
    
    def add(self, word):
        """
        Add `word` to trie
        """
        current_node = self.root

        for char in word :
            if char not in current_node.children :
                current_node.children[char] = TrieNode()
            
            current_node = current_node.children[char]
        
        current_node.is_word = True

    
    def exists(self, word):
        """
        Check if word exists in trie
        """
        current_node = self.root

        for char in word :
            if char not in current_node.children :
                return False
            else :
                current_node = current_node.children[char]

        return current_node.is_word

word_list = ['apple', 'bear', 'goo', 'good', 'goodbye', 'goods', 'goodwill', 'gooses'  ,'zebra']
word_trie = Trie()

# Add words
for word in word_list:
    word_trie.add(word)

# Test words
test_words = ['bear', 'goo', 'good', 'goos']
for word in test_words:
    if word_trie.exists(word):
        print('"{}" is a word.'.format(word))
    else:
        print('"{}" is not a word.'.format(word))