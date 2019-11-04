#1
n = int(input('n='))
for i in range(1, n):
    if i % 2 == 0:
        print(i)

#2
dict_var = {'country1': 'capital1',
            'country2': 'capital2',
            'country3': 'capital3',
            'country4': 'capital4',
            'country5': 'capital5'}
list_country = list(['country1', 'country2', 'country3', 'country5'])
for i in list_country:
    if i in dict_var:
        print(dict_var[i])

#3
for i in range(1, 101):
    if i % 15 == 0:
        print('FizzBuzz')
    elif i % 5 == 0:
        print('Buzz')
    elif i % 3 == 0:
        print('Fizz')
    else:
        print(i)

#4


def bank(many, year, percent):
    sum_many = many
    for i in range(1, year+1):
        sum_many += (sum_many*percent/100)
    print('Сумма по истечению депозита:', round(sum_many, 2))


bank(int(input('Сумма вклада:')), int(input('На сколько лет:')), int(input('Процентная ставка:')))