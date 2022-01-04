# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.

def is_palindrome(x):
    x = str(x)
    y = x [::-1]
    return x == y

i = 999
x = i * 999
while(not is_palindrome(x)):
    i -= 1
    x = i * 999

print("{}x999".format(i))
print(x)
