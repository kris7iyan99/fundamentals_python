def solve(a,b,c):
    sum_result = add(a,b)
    result = subtract(sum_result, c)
    return  result

def add (a, b):
    return a+b
def subtract (a, b):
    return a-b


a = int(input())
b = int(input())
c = int(input())


res = solve(a, b, c)
print(res)