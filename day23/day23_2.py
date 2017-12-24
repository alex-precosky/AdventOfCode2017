b = 107900
c = 124900

# finds prime numbers between b and c

num_primes = 0
num_non_primes = 0

primes = set()

for line in open("primes.txt", "r").readlines():
    splitline = line.strip().split('\t')
    for prime in splitline:
        primes.add(int(prime))

for i in range(b, c+1, 17):
    if i in primes:
        num_primes += 1
    else:
        num_non_primes += 1

print(f"num primes: {num_primes}   num non primes: {num_non_primes}")

