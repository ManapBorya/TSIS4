def divisible_by_3_and_4(n):
     for num in range(n + 1):
       if num % 3 == 0 and num % 4 == 0:
             yield num
n = 20
for num in divisible_by_3_and_4(n):
    print(num)
