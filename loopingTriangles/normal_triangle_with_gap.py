n=5
b=1
for i in range(n):
    for j in range(i,n):
     print(" ",end=" ")
    for k in range(i+1):
     print("*",end=" ")
    for l in range(b):
      print(" ",end=" ")
    for m in range(i+1):
     print("*",end=" ")
    
    print()
