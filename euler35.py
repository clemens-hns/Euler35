

# how many circular primes below one million?

def all_rotations(num):
	#print "Testing for Circular Prime: ", num
	if(isPrime(num) == False):
		return False
	for i in range(1, len(str(num))):
		num = rotat3(num)
		#print num
		if(isPrime(num) == False):
			return False
	#print "Circular: ", num
	return True

def rotat3(num):
	num=str(num)
	length = len(num)
	num=num[length-1] + num[0:length-1]
	return int(num)
	
def isPrime(n):
  if n == 2 or n == 3: return True
  if n < 2 or n%2 == 0: return False
  if n < 9: return True
  if n%3 == 0: return False
  r = int(n**0.5)
  f = 5
  while f <= r:
    #print '\t',f
    if n%f == 0: return False
    if n%(f+2) == 0: return False
    f +=6
  return True    
  
count = 0
for n in range(2, 1000000):
	if(all_rotations(n) == True):
		count = count + 1
print "Count: ", count