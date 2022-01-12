for x in range(0, 151):
    print(x)

print(*range(5,1001, 5))

for i in range(0,101):
    if i % 5 == 0:
        print("Coding")
    elif i %10 ==0:
        print("Coding Dojo")
    else:
        print(i)

sum = 0
for y in range(0, 500000,1):
    sum+=y
    print(sum)
    

for var in range(2018, 0, -4):
    if var> 0:
        print(var)

lowNum = 2
highNum = 9
mult = 3

for n in range(lowNum,highNum + 1):
    if n % mult == 0:
        print(n)
    

