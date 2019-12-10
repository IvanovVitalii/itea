# Calculate payments by term and percentage


def bank(many, year, percent):
    sum_many = many
    for i in range(1, year+1):
        sum_many += (sum_many*percent/100)
    print('Сумма по истечению депозита:', round(sum_many, 2))


bank(int(input('Сумма вклада:')), int(input('На сколько лет:')), int(input('Процентная ставка:')))
