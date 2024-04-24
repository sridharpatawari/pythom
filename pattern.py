#pattern1
for i in range(1,6):
    for j in range(1,i+1):
        print('*',end=' ')
    print()
    
    
#patter2
n=int(input())
for i in range(1,n+1):
    for j in range(i,n+i):
        print(j,end=" ")
    print()


#patter3
n=int(input())
for i in range(1,n+1):
    for j in range(i,n+i):
        print(chr(64+j),end=" ")
    print()


#pattern4
n=int(input())
for i in range(1,n+1):
    for j in range(0,n):
        print(chr(64+j),end=" ")
    print()

#pattern5
n=int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

#patter6
n=int(input())
for i in range(1,n+1):
    for j in range(i,i+i):(or)for j in range(i,2*i):
        print(j,end=" ")
    print()


#pattern7
n=int(input())
for i in range(n):
    for j in range(n,i,-1):
        print(j,end=" ")
    print()


#patter8
n=int(input())
for i in range(n):
    for j in range(n):
        print("*",end=" ")
    print()



#patter9
n=int(input())
for i in range(n):
    if i==0 or i==n-1:
        for j in range(n):
            print("*",end=" ")
        print()
    else: 
        for j in range(n):
            if j==0 or j==n-1:
                print("*",end=" ")
            else: 
                print(" ",end=" ")
        print()


#patter10
n=int(input())
for i in range(n):
    if i==0 or i==1 or i==n-1 or i==n-2:
        for j in range(n):
            print("*",end=" ")
        print()
    else: 
        for j in range(n):
            if j==0 or j==1 or j==n-1 or j==n-2:
                print("*",end=" ")
            else: 
                print(" ",end=" ")
        print()



