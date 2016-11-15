

def braces_are_correct(string):
    import collects.stack as _stack
    stack = _stack.Stack()
    for ch in string:
        if ch == '(' or ch == '[' or ch == '{' or ch == '<':
            stack.push(ch)
        elif ch == ')' or ch == ']' or ch == '}' or ch == '>':
            if stack.is_empty():
                return False
            previous_ch = stack.pop()
            if ch == '(' and  previous_ch != ')':
                return False
            if ch == '[' and  previous_ch != ']':
                return False
            if ch == '{' and  previous_ch != '}':
                return False
    return True


string = input("Enter a sequence\n")

print ("Your sequence:\n" + string)

if braces_are_correct(string):
    print ("Correct")
else:
    print ("Incorrect!")
