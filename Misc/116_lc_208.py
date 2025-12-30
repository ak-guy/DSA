class TrieNode:
    def __init__(self):
        self.node = [None for _ in range(26)]
        self.endFlag = False

    def containsKey(self, c):
        return self.node[ord(c) - ord("a")] != None

    def putKey(self, c):
        self.node[ord(c) - ord("a")] = TrieNode()

    def getCharReferenceNode(self, c):
        return self.node[ord(c) - ord("a")]

    def getEndFlag(self):
        return self.endFlag

    def setEndFlag(self, val):
        self.endFlag = val


class Trie:
    def __init__(self):
        self.rootNode = TrieNode()

    def insert(self, word):
        node = self.rootNode
        for char in word:
            if not node.containsKey(char):
                node.putKey(char)
            node = node.getCharReferenceNode(char)
        node.setEndFlag(True)

    def search(self, word):
        node = self.rootNode
        for char in word:
            if not node.containsKey(char):
                return False
            node = node.getCharReferenceNode(char)
        return node.getEndFlag()

    def startsWith(self, prefix):
        node = self.rootNode
        for char in prefix:
            if not node.containsKey(char):
                return False
            node = node.getCharReferenceNode(char)
        return True
