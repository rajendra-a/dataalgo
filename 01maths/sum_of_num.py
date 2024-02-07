
# naive solution
def sum_of_num(n):
    sum = 0
    i = 1
    while i <= n:
        sum = sum + i
        i = i + 1
    return sum 



print(sum_of_num(2))

# Time complexity: O(n)
# Space complexity: O(1)


# Efficient program for finding n natural numbers

def find_n_num(n):
    return n*(n+1)/2

print(find_n_num(7))

# Time complexity: O(1)
# Space complexity: O(1)

# The above program overflow, even if the result is not beyond the integer limit. We can avoid overflow up to some
# some extent by deviding first

def sum_of_n_num(n):
    if (n % 2 == 0):
        return n/2*(n+1)                                             
    else:
        return ((n+1)/2) * n
    

        