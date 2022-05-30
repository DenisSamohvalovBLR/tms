# Написать функцию month_to_season(), которая принимает 1 аргумент - номер месяца - и возвращает название сезона,
# к которому относится этот месяц. Например, передаем 2, на выходе получаем "Winter".

def month_to_season(month_number):
    season_name = {
        (12, 1, 2): "Winter",
        (3, 4, 5): "Spring",
        (6, 7, 8): "Summer",
        (9, 10, 11): "Autumn"
    }
    for key, value in season_name.items():
        if month_number in key:
            return value
