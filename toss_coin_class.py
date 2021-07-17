# Бросаем монету с помощью методов класса.
from random import choice


class Coin:
    sides = ['Орёл', 'Решка']
    statistics = {'times': 0,
                  'observe': 0,
                  'reverse': 0}

    def __init__(self):
        print('Вот новая монета для бросания.')

    @classmethod
    def toss(cls):
        print('Бросаем монету...')
        result = choice(Coin.sides)
        Coin.statistics['times'] += 1
        if result == 'Орёл':
            Coin.statistics['observe'] += 1
        else:
            Coin.statistics['reverse'] += 1
        print(f'...{result}!')

    @classmethod
    def stats(cls):
        print(f'Монета брошена: {Coin.statistics["times"]:3d} раз(а);')
        print(f'- орёл выпал:   {Coin.statistics["observe"]:3d} раз(а);')
        print(f'- решка выпала: {Coin.statistics["reverse"]:3d} раз(а).')


new_coin = Coin()
new_coin.toss()
new_coin.toss()
new_coin.toss()
new_coin.toss()
new_coin.toss()
new_coin.stats()
new_coin.toss()
new_coin.toss()
new_coin.toss()
new_coin.toss()
new_coin.toss()
new_coin.stats()
