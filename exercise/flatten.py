"""mod doc """
import json
def flatten(txt):
    """doc"""
    result = []
    for i in txt:
        if isinstance(i, int):
            result.append(i)
        else:
            result.extend(flatten(i))
    return result
lst = flatten(json.loads(input()))
lst.sort(reverse=True)
print(lst)
