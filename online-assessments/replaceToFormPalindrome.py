# Write a function that, given a string S of length N, returns any palindrome which can be obtained by replacing all of
# the question marks in S by lowercase letters ('a'-'z'). If no palindrome can be obtained, the function should return
# 'NO'

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# Time complexity: O(n)
# Space complexity: O(n)
def solution(S: str) ->  str:
    # Did not take into account '?' in the middle
    
    output = ''

    for i in range(len(S) // 2):
        if S[i] == '?' or S[-1-i] == '?':
            if S[i] == '?' and S[-1-i] != '?':
                output += S[-1-i]
            elif S[i] != '?' and S[-1-i] == '?':
                output += S[i]
            else:
                output += 'a'
        elif S[i] == S[-1-i]:
            output += S[i]
        else:
            return 'NO' 

    middle: str = ''

    if len(S) % 2 == 1:
        middle = S[len(S) // 2] if S[len(S) // 2] != '?' else 'a'

    return output + middle + output[::-1]

def main():
    print('Expected: "aabbaa"')
    print(f'Output  : "{solution("?ab??a")}"')

    print('Expected: "NO"')
    print(f'Output  : "{solution("bab??a")}"')

    print('Expected: "aaa"')
    print(f'Output  : "{solution("?a?")}"')

    print('Expected: "aaa"')
    print(f'Output  : "{solution("a?a")}"')
    
    print('Expected: "aaa"')
    print(f'Output  : "{solution("???")}"')

    print('Expected: "a"')
    print(f'Output  : "{solution("a")}"')

if __name__ == "__main__":
    main()