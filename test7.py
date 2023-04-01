#題目 歡迎使用拉麵點餐機~
#print("abcd".upper()) #變為大寫
#print("ABCD".lower()) #變為小寫

#nod = 拉麵 #big = 加大 #egg = 加蛋 #meat = 加肉
print("歡迎使用拉麵點餐機~")
print("(1) 鹽味拉麵 $220")
print("(2) 醬油拉麵 $240")
print("(3) 豚骨拉麵 $280")

nod = input("請選擇拉麵口味 (輸入:1 or 2 or 3) ")
big = input("是否加大(輸入:Y or N) ").upper() #將小寫變為大寫
soup = input("豚骨口味+$50 其他口味+$30 (輸入:A(豚骨) or B(其他))").upper()
egg = input("是否要加糖心蛋+$30 (輸入:Y or N)").upper()
meat = input("是否加叉燒+$60 (輸入:Y or N)").upper()

money = 0
if nod == "1":
    money += 220

elif nod == "2":
    money += 240

elif nod == "3":
    money += 280

if big =="Y":       
    
    if soup =="A":
        money += 50
    elif soup =="B":
        money += 30
    
if egg == "Y":
    money += 30
elif egg == "N":
    money += 0

if meat == "Y":
    money += 60
elif meat =="N":
    money += 0

if big == "Y" and egg =="Y" and meat == "Y":
    money -= 20
    print(f"加好加滿折價$20，總金額{money}元，感謝你的光臨")

else:
     print(f"總金額{money}元，感謝你的光臨")
