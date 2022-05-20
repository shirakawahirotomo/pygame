import random
def numCheck(indata, ans):
    if indata == ans:
        print("当たり！")
        return True
    elif indata < ans:
        print("もっと大きいよ")
        return False
    else:
        print("もっと小さいよ")
        return False

ans = random.randint(1,100)
flag = True
while flag:
    userdata = int(input("1〜100のいくつだと思いますか？"))
    if numCheck(userdata, ans) == True:
        flag = False