# Print table of a number

print("Table of which number")
a=int(input())
#b=int(a)
print("Upto which number")
#b=input()
#c=int(b)
#c=c+1
#print (c)
for n in range(1,11):
    m=a*n
    #print(m)
    print ("%s * %s = %s" % (a,n,m))


