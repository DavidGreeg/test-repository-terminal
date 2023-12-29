def fibonacci(n:int,memo:dict)->int:
	#return 1 if n<=1 else memo[n]=fibonacci(n-1,memo) + fibonacci(n-2,memo)
	if n <=1:
		return 1
	if n not in memo:
		memo[n]= fibonacci(n-1, memo) + fibonacci(n-2, memo)
	return memo[n]

if __name__ == "__main__":
	memo=dict()
	for n in (1,2,3,5,1000):
		print(f"Fibonacci de {n}: {fibonacci(n,memo)}") 
