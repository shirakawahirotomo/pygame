import random
a = random.randint(1,15)
b = random.randint(1,15)
print("問"*a +"間"+"問"*b )
num = int(input("間は、左から何番目にありますか？"))
if num == a + 1:
	print("正解！")
else:
	print("間違い",a+1,"番目です。")