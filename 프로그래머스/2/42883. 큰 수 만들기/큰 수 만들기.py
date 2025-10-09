from collections import deque

def solution(number, k):
    stack = []
    n = len(number)
    tmp_k = k
    for num in number:
        while stack and k > 0 and stack[-1] < num:
            stack.pop()
            k -= 1
        stack.append(num)

    return ''.join(stack[:n-tmp_k])