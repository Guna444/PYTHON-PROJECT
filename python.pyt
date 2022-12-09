a=int(input("enter lower range: "))
b=int(input("enter upper range: "))
print("Range is",(a,b))
print("Then the status of each number in the range is:") 
for num in range(a,b+1):
 if num > 1:
 for i in range(2, num):
 
 if num%i==0:
 break
 else:
 print(num,"is prime number")
 continue
 if i>=2:
 print(num,"is non-prime or composite number")
 
def count_primes_nums(a,b):
 ctr=0
 for j in range(a,b):
 if j <= 1:
 continue
 for k in range(2,j):
 if (j%k) == 0:
 break
 else:
 ctr+=1
 return ctr
e=int(b+1-a)
x=count_primes_nums(a,b)
y=int(e-x)
print(x,"prime and",y,"composite numbers in the range")