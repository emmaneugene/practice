# Problem: https://leetcode.com/problems/reverse-bits/


class Solution:
    def reverseBits(self, n: int) -> int:
        reversed: int = 0

        isPositive: bool = n >= 0

        for i in range(32):
            reversed *= 2
            if n % 2 == 1:
                reversed += 1
            n //= 2
        return reversed if isPositive else -reversed
        

def main():
    s = Solution()
    print('Expected: 964176192')
    print(f'Output  : {s.reverseBits(43261596)}')
    
    print('Expected: 3221225471')
    print(f'Output  : {s.reverseBits(4294967293)}')

if __name__ == "__main__":
    main()