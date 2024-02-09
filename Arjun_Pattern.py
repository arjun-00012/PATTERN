r=int(input("enter the row:"))
c=int(input("enter the col:"))
row=r*2
col=c+1
for i in range(row):
    for j in range(col):
        if i%2!=0:
            if j%2==0:
                print("/",end="")
            if j%2!=0:
                print("   \\",end="")
            if j%2!=0:
                if j<c:
                    print("___",end="")
        if i==0:
            if j%2!=0:
                print(" ___",end="    ")
    print("")
    for k in range(col):
        if i%2!=0:
            if k%2==0:
                print("\\",end="")
            if k%2!=0:
                print("___/   ",end="")
print("")