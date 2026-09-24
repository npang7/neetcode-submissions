class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for ch in s:
                count[ord(ch) - ord("a")] += 1
            key= tuple(count)
            group[key].append(s)
        return list(group.values()) # List[List[str]]