import random
dish1 = ["キムチ鍋","豆乳クリーム煮","おでん","ふんわり卵のあんかけうどん","ポトフ"]
dish2 = ["厚揚げの酢豚風","豚肉と玉ねぎのポン酢炒め","炊き込みご飯","鶏モモみぞれ煮"]
dish3 = ["トマトツナそうめん","バターチキンカレー","うなぎの錦糸丼","夏野菜のガスパチョ"]

print("今日の夕食をご提案します。")
temp = int(input("今日の気温は何度ですか?"))
if temp < 15:
	dish = random.choice(dish1)
	print("今日は寒いので",dish,"はいかがでしょう。")
elif temp < 28:
	dish = random.choice(dish2)
	print("今日は快適なので", dish, "はいかがでしょう。")
else:
	dish = random.choice(dish3)
	print("今日は暑いので", dish, "はいかがでしょうか。")