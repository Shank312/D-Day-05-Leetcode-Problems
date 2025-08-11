
class Solution:
    def countPrimes(self, n: int) -> int:
        """
        Counts the number of prime numbers less than a given number n
        using the Sieve of Eratothenes algorithm.

        Args:
             n (int): The upper limit (non-inclusive) to count primes below.

        Returns:
             int: The count of prime numbers less than n.

        """

        # Step 1: Handle small cases where no prime number exist
        if n <= 2:
            return 0     # No prime number less than 2
        
        # Step 2: Create a boolean array of 'is_prime' of size n
        # Initially, assume all numbers from 0 to n-1 are prime
        is_prime = [True]*n

        # Step 3: 0 and 1 are not prime numbers
        is_prime[0] = is_prime[1] = False

        # Step 4: Start checking from the first prime number, 2
        i = 2
        # Only need to check up to sqrt(n) 
        while i*i < n:
            if is_prime[i]:
                # Step 5: If i is prime, mark the all multiples of i as not prime
                # Start from i*i because smaller multiples were already marked by smaller primes
                for j in range(i*i, n, i):
                    is_prime[j] = False

                # Step 6: Move to the next number
                i += 1
        # Step 7: Count the numbers still marked as the prime
        return sum(is_prime)

           

# Uploaded codes

class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        
        is_prime = [True] * n
        is_prime[0] = is_prime[1] = False
        
        i = 2
        while i * i < n:
            if is_prime[i]:
                for j in range(i * i, n, i):
                    is_prime[j] = False
            i += 1
        
        return sum(is_prime)
