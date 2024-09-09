package Misc;

/*
 * 241. Different Ways to Add Parentheses
 */
import java.util.*;
class Solution {
    private int compute(int n1, char operator, int n2) {
        if (operator == '+') return n1+n2;
        if (operator == '-') return n1-n2;
        if (operator == '*') return n1*n2;
        return 0;
    }

    private List<Integer> memoized(String expression, Map<String, List<Integer>> dp) {
        if (dp.containsKey(expression)) return dp.get(expression);
        List<Integer> res = new ArrayList<>();
        boolean operatorFlag = false;
        for (int i=0; i<expression.length(); i++) {
            Character ch = expression.charAt(i);
            if (!Character.isDigit(ch)) {
                operatorFlag = true;
                List<Integer> leftOperand = memoized(expression.substring(0,i), dp);
                List<Integer> rightOperand = memoized(expression.substring(i+1), dp);

                for (int n1: leftOperand) {
                    for (int n2: rightOperand) {
                        res.add(compute(n1, ch, n2));
                    }
                }
            }
        }
        if (!operatorFlag) {
            res.add(Integer.parseInt(expression));
        }
        dp.put(expression, res);
        return res;
    }

    public List<Integer> diffWaysToCompute(String expression) {
        Map<String, List<Integer>> dp = new HashMap<>();
        return memoized(expression, dp);
    }
}