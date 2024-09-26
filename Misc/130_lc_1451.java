import java.util.Arrays;

/*
 * 1451. Rearrange Words in a Sentence
 */

class Solution {
    public String arrangeWords(String text) {
        // Convert to lowercase
        text = text.toLowerCase();
        String[] words = text.split(" ");
        Arrays.sort(words, (a,b) -> Integer.compare(a.length(), b.length()));
        StringBuilder res = new StringBuilder(String.join(" ", words));

        res.setCharAt(0, Character.toUpperCase(res.charAt(0)));
        
        return res.toString();
    }
}
