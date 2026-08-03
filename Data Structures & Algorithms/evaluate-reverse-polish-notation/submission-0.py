class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operation = ""
        for token in tokens:
            # print(stack)
            if len(stack) >= 2:
                if token in ["+","-","*","/"]:
                    num2 = stack.pop()
                    num1 = stack.pop()
                    match(token):
                        case "+": stack.append(num1+num2)
                        case "-": stack.append(num1-num2)
                        case "*": stack.append(num1*num2)
                        case "/": stack.append(math.trunc(num1/num2))
                else:
                    stack.append(int(token))

            else:
                stack.append(int(token))
        return stack[0]