class Solution:
    def superpalindromesInRange(self, left, right):
        # Convert limits to integers
        L = int(left)
        R = int(right)
        ans = 0

        # Helper function to check palindrome
        def is_pal(x):
            s = str(x)
            return s == s[::-1]

        # Generate palindrome roots up to sqrt(R)
        limit = int(R ** 0.5) + 1

        # Generate even-length palindromes
        for k in range(1, 10000):
            s = str(k)
            p = int(s + s[::-1])
            p2 = p * p
            if p2 > R:
                break
            if p2 >= L and is_pal(p2):
                ans += 1

        # Generate odd-length palindromes
        for k in range(1, 10000):
            s = str(k)
            p = int(s + s[-2::-1]) 
            p2 = p * p
            if p2 > R:
                break
            if p2 >= L and is_pal(p2):
                ans += 1

        return ans


# Example test
if __name__ == "__main__":
    sol = Solution()
    print(sol.superpalindromesInRange("4", "1000"))  # Output: 4
