prompt_name = "Enter a person's name: "
name1 = input(prompt_name)
prompt_age = "Enter their age: "
age1 = int(input(prompt_age))
name2 = input(prompt_name)
age2 = int(input(prompt_age))
if age1 > age2:
    print(name1, "is", age1-age2, "years older than", name2)
elif age1 < age2:
    print(name2, "is", age2-age1, "years older than", name1)
else:
    print(name1, "and", name2, "are the same age")