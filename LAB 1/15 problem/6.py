def fibo(n):
	if n==0:
		return 0
	elif n==1:
		return 1
	else:
		return fibo(n-1)+fibo(n-2)

n = int(input("Enter positive integer n : "))
if(n<0):
    print("Wrong input")
else: 
    print("nth fibonacci number is = %d" %fibo(n))