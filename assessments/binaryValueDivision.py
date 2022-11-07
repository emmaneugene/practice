#   Given a binary string that encodes an integer, evaluate how many operations
#   it will take for that value to become 0.
#   The operations are as follows:
#   - If the number is odd,  subtract 1
#   - If the number is even, divide by 2
#
#   The algorithm will be evaluated on both *correctness* and *performance*


def solution(S: str) -> int:
    count: int = 0

    # Convenience
    S = S.lstrip('0')

    # Edge case
    if len(S) == 0:
        return 0

    # Check from LSB to MSB
    for i in range(len(S)):
        # If LSB is 1 we take an additional operation to subtract 1, making the number even
        if S[-i-1] == '1':
            count += 1
        # 1 Operation to divide an even number
        count += 1

    # Subtract 1 because we do not need to divide once we subtract from the MSB
    return count-1


if __name__ == '__main__':
    print('Expected: 7')
    print(f'Actual  : {solution("011100")}')

    print('Expected: 5')
    print(f'Actual  : {solution("111")}')

    print('Expected: 0')
    print(f'Actual  : {solution("0000")}')
