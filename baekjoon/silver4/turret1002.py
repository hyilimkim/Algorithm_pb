f = open("baekjoon_test_input/turret1002_input",'r')
n=int(f.readline())
# n=int(input())
for i in range(n):
    print("case"+str(i+1))
    a=list(map(int,(f.readline()).split()))
    # a = list(map(int, input()))
    p_l=(a[0]-a[3])**2 + (a[1]-a[4])**2
    r_l=((a[2]-a[5])**2)
    o_l=(a[2]+a[5])**2
    if (p_l==0):
        if (a[2]==a[5]):
            print("-1")
        else:
            print("0")
    elif (r_l > p_l):
        print("0")
    elif (r_l==p_l):
        print("1")
    elif (r_l<p_l):
        if (p_l==o_l):
            print("1")
      
        elif (p_l<o_l):
            print("2")
        else:
            print("0")

f.close()