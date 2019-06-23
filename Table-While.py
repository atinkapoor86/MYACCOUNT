# Print table of a number

print("Table of which number")
a=input()
a=int(a)
print("Upto which number")
b=input()
c=int(b)
print (c)
i=1
while i<=10:
      m=a*i
      
      
      print("%s * %s = %s" % (a,i,m))
      i+=1
      if i==11:
          break


