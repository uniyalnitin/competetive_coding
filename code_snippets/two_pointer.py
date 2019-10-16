# calculate all possible combinations of three sticks such that triangle cannot be formed with the combination
#i.e. a+b < c
a = [32, 4, 5, 1, 2, 65, 132]
n = len(a)
a.sort()
ans = 0
for j in range(1,n):
    A =[]
    for i in range(j): A.append(a[i]+a[j])
    p =0
    for k in range(j+1,n):
        while p <= i and A[p] < a[k]: p+=1
        ans += max(p, 0)
print(ans)