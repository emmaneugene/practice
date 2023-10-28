# Problem: https://leetcode.com/problems/evaluate-reverse-polish-notation/

# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        operands: list[int] = []

        for token in tokens:
            try:
                operands.append(int(token))
            except ValueError:
                op: int = operands.pop()

                if token == "+":
                    operands[-1] += op
                if token == "-":
                    operands[-1] -= op
                if token == "*":
                    operands[-1] *= op
                if token == "/":
                    intermed: float = operands[-1] / op
                    if intermed < 0:
                        operands[-1] = int(intermed.__ceil__())
                    else:
                        operands[-1] = int(intermed.__floor__())

        return operands[-1]


def main():
    s: Solution = Solution()

    print(s.evalRPN(["2", "1", "+", "3", "*"])) # 9
    print(s.evalRPN(["4","13","5","/","+"])) # 6
    print(s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))


if __name__ == '__main__':
    main()
