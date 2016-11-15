import collects.stack as stack

string = input("Enter a sequence\n")

print ("Your sequence:\n" + string)

stack = stack.Stack()

for ch in string:
    stack.push(ch)

print ("Reversed sequence:\n")

while not stack.is_empty():
    print (stack.pop(), end='')
