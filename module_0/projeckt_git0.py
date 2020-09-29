import numpy as np

def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1,101, size=(1000))
    
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)


def game_core(number):
    '''Сначала устанавливаем любое random число, а потом уменьшаем или увеличиваем его в зависимости от того, больше оно или меньше нужного.
       Функция принимает загаданное число и возвращает число попыток'''
    count = 1
    predict_min = 0
    predict_max = 100
    predict = np.random.randint(1,101)
    while number != predict:
        # В цикле происходит бинарный поиск загаданного числа "number"
        count += 1
        if number > predict:
            # Определяем нижнюю планку поиска.
            predict_min = predict
            predict += (predict_max - predict_min + 1)//2
            
        elif number < predict:
            # Определяем верхнюю планку поиска.
            predict_max = predict
            predict -= (predict_max - predict_min + 1)//2
    return(count) # выход из цикла, если угадали

score_game(game_core) # Выводим среднее количество шагов за которое алгоритм находит загаданное число





