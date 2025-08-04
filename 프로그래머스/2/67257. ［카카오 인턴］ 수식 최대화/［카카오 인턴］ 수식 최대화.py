def solution(expression):
    answer = 0
    
    tokens = []
    
    n = ""
    for ex in expression:
        if ex in ["-", "+", "*"]:
            tokens.append(n)
            tokens.append(ex)
            n = ""
        else:
            n += ex
    tokens.append(n)
            
    def to_oper(priority):
        output = []
        stack = []

        for token in tokens:
            if token.isdigit():
                output.append(token)
            else:
                while stack and priority[stack[-1]] >=  priority[token]:
                    output.append(stack.pop())
                stack.append(token)
                
        while stack:
            output.append(stack.pop())
        
        return output
    
    def evaluation(output):
        stack = []
        
        for op in output:
            if op.isdigit():
                stack.append(int(op))
            else:
                b = stack.pop()
                a = stack.pop()
                
                if op == "+":
                    stack.append(a+b)
                elif op == "-":
                    stack.append(a-b)
                else:
                    stack.append(a*b)
        
        return stack[0] if stack[0] >= 0 else -stack[0]
        
            
    priority_arr = [
        {"+": 3, "-": 2, "*": 1},
        {"+": 3, "-": 1, "*": 2},
        {"+": 2, "-": 1, "*": 3},
        {"+": 2, "-": 3, "*": 1},
        {"+": 1, "-": 2, "*": 3},
        {"+": 1, "-": 3, "*": 2}
    ]
    
    for priority in priority_arr:
        output = to_oper(priority)
        answer = max(answer, evaluation(output))
        
    
    return answer