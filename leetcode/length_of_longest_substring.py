def lengthOfLongestSubstring(s):
    longest = ""
    substr = ""
    for c in s:
        if c in substr:
            if len(substr) > len(longest):
                longest = substr
            substr = ""
        substr += c
    return len(longest)

print(lengthOfLongestSubstring("pwwkew"))
