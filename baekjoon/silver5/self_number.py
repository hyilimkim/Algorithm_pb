l=set(range(1,10000))
r=set()
for m in l:
    for k in str(m):
        m+=int(k)
    r.add(m)
h=l-r
for n in sorted(h):
    print(n)