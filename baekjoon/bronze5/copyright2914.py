a,c = map(int, input().split())
if (c == 100 or c==1):
    print(a*c)
else:
    print(a*(c-1)+1)