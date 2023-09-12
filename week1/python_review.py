print("hello world")
print("How are you doing?")
#"I'm gonna show my age" -> opens vi
x = 4
y = x/2 # y will be num.0 if ran with python 3+, prior to python 3 it will be 2, because it is seen as integer dividing integer
#y = x//2 #integer division (y contains int 2)
print("x is", x)
print("y is", y)
name = "George"
print("hello", name)
x = name
#y = x/2
user_name = input("Please enter your name: ")
print("hello", user_name)
a_number = int(input("Please enter a number: "))
print("half of", a_number, " is ", a_number/2)
print(a_number/2)
another_number = int(input("Please enter another number: "))
"""
Try statements might not be that good...
try:
    print("half of", a_number, " is ", a_number/2)
except(Exception e):
    print("Error!", e)
finally:
    print("Goodbye")
"""
# a list?
a_list = [1,2,3]
print (a_list)
a_list.append("something else")