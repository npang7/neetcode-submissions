class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        clock = 0
        while clock < len(s):
            read_pointer = clock
            while s[read_pointer] != "#" :
                read_pointer += 1

            length = int(s[clock : read_pointer])
            word = s[read_pointer+1 : read_pointer+length+1]
            clock = read_pointer + length +1
            res.append(word)
        return res
