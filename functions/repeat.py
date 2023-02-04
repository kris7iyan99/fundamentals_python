def repeat_string(word, n):

    string = word * n
    return string

word = input()
n = int(input())

res = repeat_string(word, n)
print(res)
