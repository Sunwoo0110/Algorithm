import java.util.*;

class Solution {
    public long solution(String expression) {
        long answer = 0;

        List<String> tokens = new ArrayList<>();
        String n = "";
        for (char ex : expression.toCharArray()) {
            if (ex == '+' || ex == '-' || ex == '*') {
                tokens.add(n);
                tokens.add(String.valueOf(ex));
                n = "";
            } else {
                n += ex;
            }
        }
        tokens.add(n);

        List<Map<String, Integer>> priorityList = new ArrayList<>();
        priorityList.add(Map.of("+", 3, "-", 2, "*", 1));
        priorityList.add(Map.of("+", 3, "-", 1, "*", 2));
        priorityList.add(Map.of("+", 2, "-", 1, "*", 3));
        priorityList.add(Map.of("+", 2, "-", 3, "*", 1));
        priorityList.add(Map.of("+", 1, "-", 2, "*", 3));
        priorityList.add(Map.of("+", 1, "-", 3, "*", 2));

        for (Map<String, Integer> priority : priorityList) {
            List<String> output = toPostfix(tokens, priority);
            long result = evaluate(output);
            answer = Math.max(answer, Math.abs(result));
        }

        return answer;
    }

    private List<String> toPostfix(List<String> tokens, Map<String, Integer> priority) {
        List<String> output = new ArrayList<>();
        Stack<String> stack = new Stack<>();

        for (String token : tokens) {
            if (isNumber(token)) {
                output.add(token);
            } else {
                while (!stack.isEmpty() && priority.get(stack.peek()) >= priority.get(token)) {
                    output.add(stack.pop());
                }
                stack.push(token);
            }
        }

        while (!stack.isEmpty()) {
            output.add(stack.pop());
        }

        return output;
    }

    private long evaluate(List<String> postfix) {
        Stack<Long> stack = new Stack<>();

        for (String token : postfix) {
            if (isNumber(token)) {
                stack.push(Long.parseLong(token));
            } else {
                long b = stack.pop();
                long a = stack.pop();
                long result = 0;

                switch (token) {
                    case "+": result = a + b; break;
                    case "-": result = a - b; break;
                    case "*": result = a * b; break;
                }

                stack.push(result);
            }
        }

        return stack.pop();
    }

    private boolean isNumber(String s) {
        return s.chars().allMatch(Character::isDigit);
    }
}
