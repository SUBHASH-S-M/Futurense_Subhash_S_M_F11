print("enter thee length of list")
n=int(input())
lis=[]
for i in range(n):
    c=input()
    lis.append(c)
def output(lis):
    for i in range (len(lis)):
        if(i<len(lis)-2):
            print(lis[i]+",",end='')
        elif (i==len(lis)-2):
            print(lis[i],end=' and ')
        else:
            print(lis[i])
output(lis)
