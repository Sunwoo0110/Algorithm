def solution(numbers):
    n = len(numbers)
    answer = [-1] * n   # 정답을 -1로 초기화
    stack = []   

    for i in range(n-1, -1, -1):  # 오른쪽에서 왼쪽으로 탐색
        while stack and numbers[stack[-1]] <= numbers[i]:
            stack.pop()  # 나보다 작거나 같은 수는 필요 없음

        if stack:  # 남아있는 수 중 가장 가까운 큰 수
            answer[i] = numbers[stack[-1]]

        stack.append(i)

    return answer
