"""desired output:
Element #1: 1
Element #2: 2
Element #3: 3
Element #4: something else
"""
# range(start,stop,step)
a_list = [1,2,3,"something else"]
for i in range(4):
	print("Element #" + str(i + 1) + ":", a_list[i])

