class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}

        for word in strs:
            chars = [0] * 26
            for letter in word:
                chars[ord(letter) - ord('a')] += 1
            
            t_chars = tuple(chars)
            if t_chars in d:
                d[t_chars].append(word)
            else:
                d[t_chars] = [word]
        
        return [i for i in d.values()]