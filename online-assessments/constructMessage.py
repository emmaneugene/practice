# Inputs:
#   S - an array of chars
#   A - an array of ints
#
#   In this problem, we have people numbered 0 ... N-1, a char array S of size
#   N, and an int array A of size N. Each person is assigned a letter in array S
#   which is indexed by their number. They are also assigned the index of the
#   next person in the sequence in array A.
#
#   Starting from the first person, we continuously append characters to a
#   message string until the 0th person isreached. Then, return the constructed
#   string
#
#   The algorithm will be evaluated only on *correctness*


def solution(S, A) -> str:
    message = S[0]
    next_person_idx = A[0]

    while next_person_idx != 0:
        next_char = S[next_person_idx]
        message += next_char
        next_person_idx = A[next_person_idx]

    return message

def main():
    S = 'cdeo'
    A = [3, 2, 0, 1]
    print('Expected: code')
    print(f'Actual  : {solution(S, A)}')

    S = 'cdeenetpi'
    A = [5, 2, 0, 1, 6, 4, 8, 3, 7]
    print('Expected: centipede')
    print(f'Actual  : {solution(S, A)}')

    S = 'bytdag'
    A = [4, 3, 0, 1, 2, 5]
    print('Expected: bat')
    print(f'Actual  : {solution(S, A)}')

if __name__ == '__main__':
    main()