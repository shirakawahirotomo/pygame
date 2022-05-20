#coding:shift-jis
state=["電車に乗っていて目的地に着いたのに、余りにも混んでて降りられなかったことがある。",
       "待ち合わせに連絡もせずに、３時間以上人を待たせたことがある。",
       "やりたくもないのに、学級委員長をやらされたことがある。",
       "あなたは天下泰平。世間の目なんて気にしない！何があっても動じない鋼の心臓を持っている！",
       "あなたの性格はいたって普通。周りに配慮しつつも抑えるところはキチンを抑える。うーん大人！",
       "あなたは小心者。常に環境に流されまくり、気がついたら立ち往生なんてしょっちゅうあるよね。"]
print("1:yes 2:no")

print(state[0])

while True:
    print("指定された数字で選択をしなさい")
    a = input()
    if (a == "1"):
        whileTrue:
            print(state[2])
            print("1:yes 2:no")
            print("指定された数字で選択をしなさい")
            b = input()
            if (b == "1"):
                print(state[5])
                break
            elif (b == "2"):
                print(state[4])
                break
    elif (a == "2"):
        print(state[1])
        print("1:yes 2:no")
        print("指定された数字で選択をしなさい")
        c = input()
        if (c == "1"):
            print(state[3])
            break
        elif (c == "2"):
            print(state[4])
            break
    else:
        continue