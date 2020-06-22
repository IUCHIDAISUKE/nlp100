s = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
nums = [1, 5, 6, 7, 8, 9, 15, 16, 19]

words = s.split()
ans = {i[0] if num+1 in nums else i[:2]: num+1 for num, i in enumerate(words)}
print(ans)
