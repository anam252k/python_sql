upto = int(input("Enter range: "))

sum1 = 0

for num in range(2, upto + 1):
    
    for i in range(2, num):
        if (int(num % i) == 0):
            break
    else:
        sum1 += num

print("\nsum is:", sum1)
