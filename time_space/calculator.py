def calculator():
    num = int(input())
    result = 0
    for i in range(num):
        result += len(str(i+1)) + 1
    print(result)

calculator()
