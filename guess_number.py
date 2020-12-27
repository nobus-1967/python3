import random
number = random.randint(1,20)
guess = int(input("Загадано число от 1 до 20. Какое? >>> "))
while guess != number:
    if guess < number:
        print("\n:( Ваше число слишко маленькое...\n")
    else:
        print("\n:( Ваше число слишком большое...\n")
    guess = int(input("Попытайтесь угадать ещё раз... >>> "))
print("\n:) Поздравляем! Правильный ответ!")
