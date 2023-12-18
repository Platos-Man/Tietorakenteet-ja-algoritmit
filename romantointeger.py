class Solution:
    def romanToInt(self, s: str) -> int:
        total = 0
        r = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        num_list = [r[letter] for letter in s]
        for idx, num in enumerate(num_list):
            if idx + 1 == len(num_list):
                total += num
                print("add", num)
            elif num < num_list[idx + 1]:
                total += -num
                print("sub", num)
            else:
                total += num
                print("add", num)
        return total


S = Solution()
print(S.romanToInt("MMCCCXCIX"))  # 2399
