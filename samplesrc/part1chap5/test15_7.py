import random
flag = True
while flag:
    dice = random.randint(1,6)
    print(dice)
    if dice == 6:
        flag = False