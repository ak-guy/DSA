'''
792. Number of Matching Subsequences
'''

'''
The solution uses a dictionary to map the first character of each 
word to lists of words starting with that character. It then iterates 
through each character in the main string s, and for the current 
character char, it retrieves and clears the list of words waiting 
for char. For each word in this list, if the word length is 1, 
it means the entire word has been matched as a subsequence, 
so the count is incremented. Otherwise, the word is truncated by 
removing the matched character at the front, and the truncated word 
is appended back into the dictionary under the key of its new first 
character. This approach efficiently advances the matching of all 
words in parallel as s is scanned once, thereby counting how many 
words are subsequences without repeatedly scanning s for each word. 
The solution has an overall time complexity roughly proportional to 
the sum of lengths of s and all words combined, making it efficient 
for this problem.
'''

from collections import defaultdict
from typing import List


class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        count = 0
        word_map = defaultdict(list)
        for word in words:
            word_map[word[0]].append(word)
        
        for char in s:
            char_word_list = word_map[char]
            word_map[char] = []
            for word in char_word_list:
                if len(word) == 1:
                    count += 1
                else:
                    word_map[word[1]].append(word[1:])
        
        return count