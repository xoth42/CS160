s = "Enter a number: "

sum = 0
while 1:
    inp = float(input(s))
    if inp < 0:
        print(sum)
        exit(0)
    sum += inp
        
