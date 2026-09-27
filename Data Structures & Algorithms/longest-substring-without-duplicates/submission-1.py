class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        longest = 0
        l = 0

        for r in range(len(s)):
            while s[r] in chars:
                chars.remove(s[l])
                l += 1

            chars.add(s[r])
            longest = max(longest, r - l + 1)

        return longest

# I use a sliding window with two pointers and a set. The set stores the characters in the current window.

# I move the right pointer through the string. If the character at the right pointer is already in the set, I remove characters from the left side and move the left pointer forward until the duplicate is gone.

# Then I add the current character to the set and calculate the current window length as `right - left + 1`. If it is greater than the maximum length, I update the maximum.

# After the right pointer reaches the end of the string, I return the maximum length. The time complexity is O(n), and the space complexity is O(n).