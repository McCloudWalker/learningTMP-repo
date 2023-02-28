import random
import array
greeter="HelloWorld!"
print(greeter)
name=input("name:")
password=input("password:")
mygen=[1,2]
key = random.choice(mygen)
print(key)
answer=input("answer:")
if name=="admin" and password=="1234":
    if key==1 and answer=="a":
        print("thinking... \n so far so good....")
    elif key==2 and answer=="b":
        print("thinking... \n so far so good....")       
    else:
        print("so sorry bad key")
        exit()   
else:
    print("so sorry bad name or password")
    exit()
print("   Just keep Swimming.....")

# Print each letter in a string
for letter in "Hello":
    print(letter, end=" ")
for letter in name:
        print(letter, end=" ")

# Print each number in a list
numbers = [1, 2, 3]
for number in numbers:
    print(number, end=" ")
else:
    print()    

# Print numbers from 0 to 9 using range
for i in range(10):
    print(i, end=" ")
else:
    print() 


import itertools
for x in itertools.permutations("ABCDEF"):
    print(x)


print("Hello", end=",") # prints Hello without a newline
print("World") # prints World on the same line as Hello

print("a", "b", "c", sep="+") # prints abc without spaces between them a +