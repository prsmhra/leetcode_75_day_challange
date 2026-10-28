class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        """Greatest common divisor of string

        Args:
            str1 (str): Dividing String 
            str2 (str): DIvisor String

        Returns:
            str: Common divisor string
        """
        for i in range(min(len(str1), len(str2)), 0, -1):
            pattern = str2[:i]
            if self.check_divisor(pattern, str1) and self.check_divisor(pattern, str2):
                return pattern
        return ""

    def check_divisor(self, pattern: str, target: str) -> bool:
        """Check if the divisor is a common divisor of both strings

        Args:
            str1 (str): Dividing String
            divisor (str): Potential common divisor

        Returns:
            bool: True if the divisor is a common divisor, False otherwise
        """
        concatenated = ""
        while len(concatenated) < len(target):
            concatenated += pattern

        return concatenated == target

if __name__ == "__main__":
    str1_list: list[str] = ["ABCABC", "ABABAB", "LEET", "ABCDEF"]
    str2_list: list[str] = ["ABC", "ABAB", "CODE", "ABC"]
    solution = Solution()
    for str1, str2 in zip(str1_list, str2_list):
        print(solution.gcdOfStrings(str1, str2))  # Output: "ABC"