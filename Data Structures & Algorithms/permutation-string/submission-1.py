class Solution: #fixed-size sliding window
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        count1 = [0] * 26
        count2 = [0] * 26

        for i in range(len(s1)):
            count1[ord(s1[i]) - ord("a")] += 1
            count2[ord(s2[i]) - ord("a")] += 1

        if count1 == count2:
            return True

        for r in range(len(s1), len(s2)):
            count2[ord(s2[r]) - ord("a")] += 1

            l = r - len(s1)
            count2[ord(s2[l]) - ord("a")] -= 1

            if count1 == count2:
                return True

        return False

# I use a fixed-size sliding window because any permutation of `s1` must have the same length and the same character frequencies as `s1`.

# First, I create two arrays of size 26. `count1` stores the character frequencies of `s1`, and `count2` stores the character frequencies of the current window in `s2`. I first initialize `count2` using the first window of `s2`.

# Then I slide the window through `s2`. At each step, I add the new character on the right by increasing its frequency, and I remove the character that leaves the window on the left by decreasing its frequency.

# After each move, I compare `count1` and `count2`. If the two arrays are equal, the current window is a permutation of `s1`, so I return `true`. If I finish checking all the windows without finding a match, I return `false`.

# The time complexity is O(n), and the space complexity is O(1).