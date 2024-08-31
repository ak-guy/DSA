package Misc;

/*
 * 767. Reorganize String
 */

import java.util.*;

class IntCharTuple implements Comparable<IntCharTuple> {
    private final Integer number;
    private final Character character;

    public IntCharTuple(Integer number, Character character) {
        this.number = number;
        this.character = character;
    }

    public Integer getNumber() {
        return number;
    }

    public Character getCharacter() {
        return character;
    }

    @Override
    public String toString() {
        return "(" + number + ", " + character + ")";
    }

    // Define natural ordering: first by number, then by character
    @Override
    public int compareTo(IntCharTuple other) {
        int numCompare = this.number.compareTo(other.number);
        if (numCompare != 0) {
            return numCompare;
        }
        return this.character.compareTo(other.character);
    }
}

class Solution {
    public String reorganizeString(String s) {
        Map<Character, Integer> charVsCount = new HashMap<>();
        for (int ind=0; ind<s.length(); ind++) {
            char ch = s.charAt(ind);
            if (charVsCount.get(ch) != null) {
                charVsCount.put(ch, charVsCount.get(ch) + 1);
            }else {
                charVsCount.put(ch, 1);
            }
        }

        PriorityQueue<IntCharTuple> pq = new PriorityQueue<>((n1, n2) -> n2.compareTo(n1));
        for (Map.Entry<Character, Integer> entry: charVsCount.entrySet()) {
            pq.add(new IntCharTuple(entry.getValue(), entry.getKey()));
        }

        String res = "";
        while (!pq.isEmpty()) {
            IntCharTuple first = pq.poll();
            if (res.length()>0 && first.getCharacter().equals(res.charAt(res.length()-1))) {
                IntCharTuple second = pq.poll();
                if (second == null) {return "";}
                res = res + second.getCharacter();
                pq.add(first);
                if (second.getNumber() > 1) {
                    pq.add(new IntCharTuple(second.getNumber()-1, second.getCharacter()));
                }
            }else {
                res = res + first.getCharacter();
                if (first.getNumber() > 1) {
                    pq.add(new IntCharTuple(first.getNumber()-1, first.getCharacter()));
                }
            }
        }
        return res;
    }
}

class Dummy {
    
}
