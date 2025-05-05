import json
def isIntersect(a, b, c):
    for i in a:
        if i in b and i in c:
            return True
    return False

a = json.loads(input())
b = json.loads(input())
c = json.loads(input())
print(isIntersect(a, b, c))