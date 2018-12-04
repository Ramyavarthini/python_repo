number = int(input('Enter number:'))
fact_num = 1
for i in range(number, 0, -1):
        fact_num = fact_num*i
print('Factorial of',number,'is',fact_num)
