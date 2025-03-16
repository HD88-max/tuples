#Write a program to check whether the given tuple - (1,2,3,3,2,1) is a palindrome or not. If it's a palindrome, then it is the same after being reversed.

tuple = (1,2,3,4,5,6,4,3,2,1)
def palindrome(tuple):
    indexing = len(tuple) - 1
    s = 0
    while s < indexing:
        if tuple[s] != tuple[indexing]:
            return False
        s = s+1
        indexing = indexing - 1
    return True
if palindrome(tuple):
    print("It is a palindrome. ")
else:
    print("It is not a palindrome. ")