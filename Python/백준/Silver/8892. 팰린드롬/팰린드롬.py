import sys
input = sys.stdin.readline

def is_palindrome(word):
    if word == word[::-1]:
        return True
    return False
    
T = int(input())

def solution(T):
    for _ in range(T):
        N = int(input())
        word = [input().strip() for _ in range(N)]
        
        found_palindrome = False

        for i in range(N):
            for j in range(N):
                if i != j:
                    words = word[i] + word[j]
                    if is_palindrome(words):
                        print(words)
                        found_palindrome = True
                        break
        
            if found_palindrome:
                break

        if not found_palindrome:
            print(0)

solution(T)
             