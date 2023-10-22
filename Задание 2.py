salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
money_capital = 0  # Ежемесячный убыток капитала
real_money_capital = 0  # Нужная финансовая подушка
count_of_months = 0  # Cчётчик месяцев

for count_of_months in range(0, months):
    money_capital = spend * ((1 + increase) ** count_of_months) - salary
    # Счёт капитала каждый месяц
    real_money_capital += money_capital  # Счёт нужной финансовой подушки
    count_of_months += 1  # Счётчик месяцев

real_money_capital = round(real_money_capital, 2)  # Округление к банковскому представлению


print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", real_money_capital)
# Вывод информации
