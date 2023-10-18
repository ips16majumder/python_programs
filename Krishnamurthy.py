a=int(input("Enter a no.:"))
t=a
s=0
while a>0:
    r=a%10
    f=1
    for i in range(1,r+1):
        f=f*i
    s=s+f
    a=a//10
if t==s:
    print("Krishnamurthy no")  #A Krishnamurthy number is a number whose sum of the factorial of digits is equal to the number itself.
else:
    print("Not a Krishnamurthy no")