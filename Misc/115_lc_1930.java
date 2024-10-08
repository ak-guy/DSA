// package Misc;

/*
 * 1930. Unique Length-3 Palindromic Subsequences
 */
import java.util.*;
class Solution {
    public int countPalindromicSubsequence(String s) {
        // idea is to first calculate the first and last occurence of each unique chars in string s
        // then if first[i] < last[i] we can find all unique chars that are there in between them
        // this is because 3-length palindrom can be of two type
        // 1. same,same,same
        // 2. same,different,same
        
        int[] firstOccurence = new int[26];
        Arrays.fill(firstOccurence, Integer.MAX_VALUE);
        int[] secondOccurence = new int[26];

        for(int i=0; i<s.length(); i++) {
            char ch = s.charAt(i);
            if (firstOccurence[ch-'a'] > i) firstOccurence[ch-'a'] = i;
            if (secondOccurence[ch-'a'] < i) secondOccurence[ch-'a'] = i;
        }

        // find all unique chars between every char in string s
        int res = 0;
        for (int i=0; i<26; i++) {
            if (firstOccurence[i] >= secondOccurence[i]) continue;
            Set<Character> charset = new HashSet<>();
            String subString = s.substring(firstOccurence[i]+1,secondOccurence[i]);
            for (char c: subString.toCharArray()) {charset.add(c);}
            res += charset.size();
        }
        return res;
    }   
}