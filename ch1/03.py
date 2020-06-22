s = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
# words = s.split()
# print(*[len(i.strip(",.")) for i in words])

s = s.replace(',', '').replace('.', '')
words = s.split()
print(*[len(i) for i in words])
