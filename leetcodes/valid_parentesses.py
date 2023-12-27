from cgi import test

def vailid(string):
    stack = []
    for char in string:
        if char in linker:
            stack.append(linker[char])
        elif char in linker.values():
            if stack and stack[-1] == char:
                stack.pop()
            else:
                return False
            
    return not stack

def testing_helper(string):
    print(f"{string} ==", vailid(string))

linker = {'{': '}',
          '(': ')'}

assert vailid("(hello how are you doing)")
assert vailid("(hello how are you doing") == False

testing_helper('({hello})')
testing_helper('(hello})')