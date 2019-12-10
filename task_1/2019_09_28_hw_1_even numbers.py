# Find all even numbers from 0 to n
n = int(input('n='))
if n > 0:
    for i in range(1, n):
        if i % 2 == 0:
            print(i)
else:
    print('"n" must be greater than zero')
