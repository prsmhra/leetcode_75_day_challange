class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i, j =0, 0
        m, n = len(word1), len(word2)
        result = ''

        while i<m or j<n:
            if i < m:
                result += word1[i]
                i += 1
            if j < n:
                result += word2[j]
                j += 1
        return result

if __name__ == "__main__":
    word1_list: list[str] = ["abc", "abcd", "a"]
    word2_list: list[str] = ["pqr", "pq", "pba"]
    solution = Solution()
    for word1, word2 in zip(word1_list, word2_list):
        print(solution.mergeAlternately(word1, word2))  # Output: "apbqcr"