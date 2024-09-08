package Misc;

/*
 * 208. Implement Trie (Prefix Tree)
 */

class Node {
    public Node[] node;
    private boolean endFlag; // by default false

    public Node() {
        this.node = new Node[26];
    }

    public boolean containsKey(char c) {
        return node[c-'a'] != null;
    }

    public void putKey(char c) {
        node[c-'a'] = new Node();
    }

    public Node getCharReferenceNode(char c) {
        return node[c-'a'];
    }

    public boolean getEndFlag() {
        return this.endFlag;
    }

    public void setEndFlag(boolean val) {
        this.endFlag = val;
    }
}

class Trie {
    private Node root;
    public Trie() {
        root = new Node();
    }
    
    public void insert(String word) {
        Node node = root; // getting a new node to iterate otherwise main root will be shifted  
        for (char ch: word.toCharArray()) {
            // if char already exists in root then we only need to shift reference
            if (!node.containsKey(ch)) {
                node.putKey(ch);
            }
            node = node.getCharReferenceNode(ch); // shifting reference node
        }
        node.setEndFlag(true);
    }
    
    public boolean search(String word) {
        Node node = root;
        for (char ch: word.toCharArray()) {
            if (!node.containsKey(ch)) {
                return false;
            }
            node = node.getCharReferenceNode(ch);
        }
        return node.getEndFlag();
    }
    
    public boolean startsWith(String prefix) {
        Node node = root;
        for (char ch: prefix.toCharArray()) {
            if (!node.containsKey(ch)) {
                return false;
            }
            node = node.getCharReferenceNode(ch);
        }
        return true;
    }
}

/**
 * Your Trie object will be instantiated and called as such:
 * Trie obj = new Trie();
 * obj.insert(word);
 * boolean param_2 = obj.search(word);
 * boolean param_3 = obj.startsWith(prefix);
 */