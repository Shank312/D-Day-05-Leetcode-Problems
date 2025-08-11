
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # If lengths differ, they cannot be anagrams
        if len(s) != len(t):
            print(f"Length mismatch: len(s)={len(s)} != len(t)={len(t)}")
            return False
        
        counts = {}  # Dictionary to count occurrences of each character in s

        # Count each character in s
        for ch in s:
            counts[ch] = counts.get(ch, 0) + 1
            print(f"Counting chars in s: '{ch}' -> counts: {counts}")

        # For each character in t, reduce the count from counts
        for ch in t:
            # If character not found or count exhausted, not an anagram
            if ch not in counts:
                print(f"Character '{ch}' not found in counts dictionary, returning False")
                return False
            if counts[ch] == 0:
                print(f"Character '{ch}' count is zero before decrement, returning False")
                return False

            counts[ch] -= 1
            print(f"Processing '{ch}' in t, updated counts: {counts}")

        # If we have matched all characters correctly, return True
        print("All characters matched correctly. Final counts:", counts)
        return True

sol = Solution()
print(sol.isAnagram("listen", "silent"))


