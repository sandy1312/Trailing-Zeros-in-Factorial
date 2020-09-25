num = int(input("Enter ur number:"))
count = 0
for i in range(1,7):
    n = pow(5, i)
    count = count + num // n
print(count)