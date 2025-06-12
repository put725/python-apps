import time
import random
o = "Yes"
input("反応速度を測定します。" \
    "[！！！！！]が出たら、できるだけ早くEnterキーを押してください。" \
    "準備ができたらEnterキーを押してください。")
while not(o == "No"):
    time.sleep(0.5)
    print("start")
    randomtime = random.randint(5, 15)
    time.sleep(randomtime)
    start_time = time.time()
    input_line = input("！！！！！")
    end_time = time.time()
    j = end_time - start_time
    j = round(j,4)
    if j < 0.01:
        print("不正")
    else:
        print(f"反応速度:{j}")
        time.sleep(1)
        o = input("もう一度やりますか？ [Yes or No]")
# print("終了")