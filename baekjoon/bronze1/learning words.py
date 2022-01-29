# a=input().lower()
a="aaadfd"
if len(a)<2:
    print(a.upper())
    exit()
l={}
for i in a:
    if i in l.keys():
        on=l[i]
        l[i]=on+1
    else:
        l[i]=1
print(l)
l=(sorted(l.items(),key=lambda x:x[1],reverse=True))
print(l)
if (l[0][1] in l[1]) :
    print("?")
else:
    print(l[0][0].upper())