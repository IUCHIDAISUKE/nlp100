s1 = 'パトカー'
s2 = 'タクシー'
print(*[i[0]+i[1] for i in zip(s1, s2)], sep='')
