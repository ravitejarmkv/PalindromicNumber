m = 11
for i in range(1, 100):
    mul = i * m
    n = mul
    temp=n
    rev=0
    while(n>0):
        dig=n%10
        rev=rev*10+dig
        n=n//10
    if(temp==rev):
        print(mul, "The number is a palindrome!")
