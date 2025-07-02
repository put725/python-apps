import random
o = "Yes"

c = 1
while o == "Yes":
    w = 0
    random_number = random.randint(1, 100)
    print(random_number)
    if random_number >= 70:
        if random_number >= 85:
            print("かなり大きい")
        else:
            print("大きい")
    elif random_number <= 30:
         if random_number <= 15:
             print("かなり小さい")
         else:
             print("小さい")    
    while w == 0:
        input_line = int(input("数字を入力してください:"))
        if input_line == random_number:
             print("正解")
             print(f"{c}回目で正解。")
             w = 1
        else:
            print("不正解")
        if c == 5:
            print(f"答えは{random_number}です。")
            c += 1
    o = input("もう一度やりますか？ [Yes or No]")
# print("終了")