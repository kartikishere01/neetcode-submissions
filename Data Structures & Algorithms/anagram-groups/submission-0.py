class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = {}
        for word in strs :
            sorted_words = "".join(sorted(word))
            if sorted_words in anagram:
                anagram[sorted_words].append(word)
            else:
                anagram[sorted_words]=[word]
        return list(anagram.values())
