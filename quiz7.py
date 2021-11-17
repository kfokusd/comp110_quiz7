# Function: is_prime(n)
# - Takes 1 parameter, n (integer)
# - Returns True if n is a prime number; otherwise, returns False
# TODO: Implement this function

# Function: primelist(min, max)
# - Takes 2 parameters, min, and max (integer)
# - Returns a list with prime numbers between (min) and (max) in descending order  
# - For example,  primelist(3, 10) returns [7, 5]
# - For example,  primelist(-10, 10) returns [7, 5, 3, 2]
def primelist(min, max):
    primelst = []

    # TODO: Implement this function
    return primelst 


# DO NOT change the following code
print(primelist(3, 10))
print(primelist(11, 50))
print(primelist(-10, 10))
print(primelist(-100, 100))

# Expected Output:
#[7, 5]
#[47, 43, 41, 37, 31, 29, 23, 19, 17, 13]
#[7, 5, 3, 2]
#[97, 89, 83, 79, 73, 71, 67, 61, 59, 53, 47, 43, 41, 37, 31, 29, 23, 19, 17, 13, 11, 7, 5, 3, 2]