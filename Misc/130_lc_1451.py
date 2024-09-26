'''
1451. Rearrange Words in a Sentence
'''

class Solution:
    def arrangeWords(self, text: str) -> str:
        text = text.lower()
        text = list(text.split(" "))
        text.sort(key =lambda x : len(x))
        res = " ".join(text)
        res = res[0].upper() + res[1:]

        return res