#Write a program to perform the following operations: 1. Create a tuple with different datatypes 2. Create another tuple of integers 3. Create a new tuple by adding 9 to the previous tuple 4. Count the occurrences of an element in the tuple 5. Perform slicing on the tuple

tuple1 = (1,"H",[1],bool)
print(tuple1)
tuple2 = (1,2,3,4,5,6)
print(tuple2)
tuple3 = (9)
tuple4 = (1,2,3,4,tuple3)
print(tuple4)
user = int(input("What number do you want to check the count of? "))
tuple5 = (1,1,3,4,2,2,6,3,8,8,9,8,5,6,4,3,8)
print(tuple5.count(user))
tuple6 = (1,2,3,4,5,6,7,8,9)
slice = tuple6[2:7]
print(slice)
