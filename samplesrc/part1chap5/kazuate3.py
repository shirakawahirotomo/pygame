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

count = 0
ans = random.randint(1,100)
flag = True
while flag:
    count = count + 1
    indata = int(input("1〜100のいくつだと思いますか？"))
    if numCheck(indata, ans) == True:
        flag = False
print(count, "回で当たり！")