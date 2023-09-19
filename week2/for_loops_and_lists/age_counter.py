#!/Library/Frameworks/Python.framework/Versions/3.10/bin/python3
# Loops & lists
# The teacher does not like using break statements. So that code analysis can be clearer. more causes for the while loop to be ended. A while loop with only one entry point and one exit point is like a door. a break statement is like jumping out the window. Although, if the code is so small, break statements can be used when logic is very simple. instructor has never used continue statements. when you use break and continue, and the code execution is jumping around, the code is spagetti code, and it is very hard to understand.
if __name__=='__main__':
	print("let's count from one up to your age.")
	last_year_printed = 0
	user_age = int(input("Enter your age: "))
	while last_year_printed < user_age:
		last_year_printed = last_year_printed + 1
		print(last_year_printed)
	print("now outside while loop")

