def ciper_char(c):
    if 'a' <= c <= 'z':
        c = chr(219 - ord(c))
    return c


def ciper_string(string):
    res = [chr(219 - ord(ch)) if 'a' <= ch <= 'z' else ch for ch in string]
    return ''.join(res)


s = 'test'
print(*[ciper_char(i) for i in s], sep='')
print(ciper_string(s))
