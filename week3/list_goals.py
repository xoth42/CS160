import io

file1 = open("/Users/zickers/Classwork/CS160/week3/luc_list","r",encoding="utf-8")
lines = file1.readlines()
print("What do I need to get done?")
for line in lines:
    print(line)
print("Get it done.")