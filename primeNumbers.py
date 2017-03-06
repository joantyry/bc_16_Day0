
def primeNumbers(n):
	'''
	This function defines a prime_number generator, that takes in a number between 0 and n, then outputs a list of prime_numbers within that range.
	'''
	
	if (n < 0):
		return "The number must be positive"
	elif (n == 0 or n == 1):
		return "Null"
	elif (n == ""):
		return "Input a number"	
	elif (n == 2):
		return 2
	elif (type(n)!= int):
		return "only numbers are accepted"	

	
	

	prime_list = list()
	for num in range(2, n+1):
		if all(num % i != 0 for i in range(2, num)):
			prime_list.append(num)
    	
        	
	return prime_list


print primeNumbers(10)
print primeNumbers(0)
print primeNumbers("a")