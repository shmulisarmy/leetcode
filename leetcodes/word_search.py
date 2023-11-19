class trie:
    def __init__(self):
        self.children = {}

    def insert(self, word):
        if word[0] not in self.children:
            self.children[word[0]] = trie()
        if len(word) > 1:
            self.children[word[0]].insert(word[1::])


    def search(self, word):
        if word[0] == '.':
            for i in self.children:
                if self.children[i].search(word[1::]):
                    return True
        if word[0] in self.children:
            if len(word) == 1:
                return True
            return self.children[word[0]].search(word[1::])
        return False
    


main_tree = trie()

words = ['apple', 'banana', 'carot']

for i in words: main_tree.insert(i)

print(main_tree.search('app.e'))