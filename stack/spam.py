"""mod doc"""
class ArrayStack():

    def __init__(self):
        self.size = 0
        self.data = list()

    def push(self, input_data):
        try:
            if input_data.isdigit():
                input_data = int(input_data)
            elif input_data.replace(".", "", 1).isdigit():
                input_data = float(input_data)
        except (TypeError, ValueError, ArithmeticError, AttributeError):
            pass
        finally:
            self.data.append(input_data)
            self.size += 1

    def pop(self):
        if not self.data:
            print("Underflow: Cannot pop data from an empty list")
            return None
        self.size -= 1
        return self.data.pop()


    def is_empty(self):
        if not self.data:
            return True
        return False

    def get_stack_top(self):
        if not self.data:
            print("Underflow: Cannot get stack top from an empty list")
            return None
        x = self.data.pop()
        self.data.append(x)
        return x

    def get_size(self):
        return self.size

    def print_stack(self):
        print(list(self.data))

def spamCheck():
    """main"""
    text = input()
    stack = ArrayStack()
    matching_brackets = {')': '(', ']': '[', '}': '{'}

    for char in text:
        if char in "([{":
            stack.push(char)
        elif char in ")]}":
            if stack.is_empty() or stack.pop() != matching_brackets[char]:
                stack.pop()
                return False

    return stack.is_empty()

print(spamCheck())
