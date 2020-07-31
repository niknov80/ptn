# s = '1 1 1 1 1 2 2 2'
a = int(input())
j = 0
arr = []
lst =[]
for i in range(a + 1):
    arr = [i for j in range(i)]
    lst.append(arr)
    j += i

for i in lst:
    for j in i:
        print(j)