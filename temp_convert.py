temp = float(input("請輸入溫度:"))
unit = input("請輸入單位(F/C): ")
if unit == "F":
    temp = round((temp - 32) * 5 / 9, 2)
    print("攝氏", temp, "度")

elif unit == "C":
    temp = round((temp * 5 / 9) + 32, 2)
    print("華氏", temp, "度")
else:
    print("輸入錯誤!")