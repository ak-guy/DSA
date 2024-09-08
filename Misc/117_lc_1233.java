package Misc;

/*
 * 1233. Remove Sub-Folders from the Filesystem
 */

import java.util.*;
class Node {
    public Map<String, Node> node;
    private boolean endFlag;

    public Node() {
        this.node = new HashMap<>();
    }

    public boolean containsKey(String c) {
        return node.containsKey(c);
    }

    public int getNodeLength() {
        return node.size();
    }

    public void putKey(String c) {
        node.put(c, new Node());
    }

    public Node getCharReferenceNode(String c) {
        return node.get(c);
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
    
    public boolean insert(String word) {
        String[] modWord = word.split(String.valueOf('/'));
        Node node = root; 
        for (int i=1; i<modWord.length; i++) {
            if (node.getEndFlag() == true) return false;
            if (!node.containsKey(modWord[i])) {
                node.putKey(modWord[i]);
            }
            node = node.getCharReferenceNode(modWord[i]);
            
        }
        node.setEndFlag(true);
        return true;
    }
}

class Solution {
    public List<String> removeSubfolders(String[] folder) {
        Trie t = new Trie();
        List<String> res = new ArrayList<>();
        Arrays.sort(folder);
        for (String s : folder) {
            if (t.insert(s) == true)res.add(s);
        }
        return res;
    }
}